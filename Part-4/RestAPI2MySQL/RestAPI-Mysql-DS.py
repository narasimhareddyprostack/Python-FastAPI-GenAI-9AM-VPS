import requests
import mysql.connector
from mysql.connector import Error
from typing import List, Tuple, Optional
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class UserETLProcessor:
    def __init__(self, db_config: dict):
        self.db_config = db_config
        self.rest_api_url = 'https://jsonplaceholder.typicode.com/users'
        
    def extract(self) -> Optional[List[dict]]:
        """Extract data from REST API with error handling"""
        try:
            logger.info(f"Extracting data from {self.rest_api_url}")
            response = requests.get(
                self.rest_api_url, 
                timeout=10,
                headers={'Accept': 'application/json'}
            )
            response.raise_for_status()
            
            users = response.json()
            logger.info(f"Successfully extracted {len(users)} users")
            return users
            
        except requests.exceptions.Timeout:
            logger.error("Request timeout while extracting data")
            return None
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.ConnectionError:
            logger.error("Connection error occurred. Check network connectivity.")
            return None
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request exception: {req_err}")
            return None
        except ValueError as json_err:
            logger.error(f"JSON parsing error: {json_err}")
            return None
    
    def transform(self, users: List[dict]) -> List[Tuple]:
        """Transform extracted data into database-ready format"""
        if not users:
            return []
            
        user_data = []
        for user in users:
            try:
                user_id = user.get('id')
                name = user.get('name')
                company_name = user.get('company', {}).get('name')
                
                if None in (user_id, name, company_name):
                    logger.warning(f"Skipping user with missing data: {user}")
                    continue
                    
                user_data.append((user_id, name, company_name))
                
            except (KeyError, AttributeError) as e:
                logger.warning(f"Error processing user data: {e}. User: {user}")
                continue
        
        logger.info(f"Transformed {len(user_data)} users")
        return user_data
    
    def load(self, user_data: List[Tuple]) -> bool:
        """Load transformed data into database"""
        if not user_data:
            logger.warning("No data to load")
            return False
            
        dbcon = None
        cursor = None
        success = False
        
        try:
            logger.info("Connecting to database...")
            dbcon = mysql.connector.connect(**self.db_config)
            cursor = dbcon.cursor()
            
            # Check if table exists and create if not
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    company VARCHAR(255)
                )
            """)
            logger.info("Table 'users' verified/created")
            
            # FIXED SQL: Using alias syntax for ON DUPLICATE KEY UPDATE
            sql_st = """
                INSERT INTO users(id, name, company)
                VALUES (%s, %s, %s) AS new
                ON DUPLICATE KEY UPDATE
                name = new.name,
                company = new.company
            """
            
            logger.info(f"Inserting {len(user_data)} records...")
            cursor.executemany(sql_st, user_data)
            dbcon.commit()
            
            inserted_count = cursor.rowcount
            logger.info(f"Successfully processed {inserted_count} records")
            success = True
            
        except Error as err:
            logger.error(f"Database error: {err}")
            if dbcon:
                dbcon.rollback()
            success = False
        except Exception as e:
            logger.error(f"Unexpected error during load: {e}")
            if dbcon:
                dbcon.rollback()
            success = False
        finally:
            if cursor:
                cursor.close()
            if dbcon and dbcon.is_connected():
                dbcon.close()
                logger.info("Database connection closed")
        
        return success
    
    def execute_etl(self) -> bool:
        """Execute the complete ETL process"""
        logger.info("Starting ETL process...")
        
        users = self.extract()
        if users is None:
            logger.error("Extraction failed. Aborting ETL process.")
            return False
        
        user_data = self.transform(users)
        if not user_data:
            logger.error("No valid data after transformation")
            return False
        
        if not self.load(user_data):
            logger.error("Loading failed")
            return False
        
        logger.info("ETL process completed successfully")
        return True

def main():
    # Database configuration
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': '9am',
        'raise_on_warnings': True,
        'autocommit': False
    }
    
    # Create ETL processor
    etl_processor = UserETLProcessor(db_config)
    
    # Execute ETL
    try:
        success = etl_processor.execute_etl()
        if success:
            print("ETL process completed successfully")
        else:
            print("ETL process failed. Check logs for details.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        logger.info("ETL process interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Fatal error in ETL process: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()