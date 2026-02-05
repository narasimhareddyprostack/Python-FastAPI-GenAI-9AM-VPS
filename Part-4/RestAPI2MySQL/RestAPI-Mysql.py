import requests
import mysql.connector
#Extract
rest_api_url='https://jsonplaceholder.typicode.com/users'
users=requests.get(rest_api_url).json()

#Tranform
user_data=[]
for user in users:
    user_data.append((user['id'],user['name'],user['company']['name']))

#Load
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='9am')
    cursor=dbcon.cursor()
    sql_st='''
                INSERT INTO users(id,name,company)
                values
                (%s,%s,%s);
            '''
    cursor.executemany(sql_st,user_data)
    dbcon.commit()
    print("Data Inserted successfully")

except mysql.connector.Error as err:
    print(err)

finally:
    cursor.close()
    dbcon.close()