import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='9am')
    if dbcon.is_connected():
        print("Connection Established")
        cursor=dbcon.cursor()
    else:
        print("Connection Failed")

except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()