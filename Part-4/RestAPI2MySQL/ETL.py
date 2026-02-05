import requests
import mysql.connector
#Extract
rest_api_url='https://jsonplaceholder.typicode.com/users'
user_resp=requests.get(rest_api_url)
print(user_resp.status_code)
users=user_resp.json()
print(type(users))
print(len(users))
#Tranform
user_data=[]
for user in users:
    id=user['id']
    name=user['name']
    company=user['company']['name']
    user_data.append((id,name,company))

print(len(user_data))
print(user_data)

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