import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='9am')
    cursor=dbcon.cursor()
    sql_st='''
            insert into employee
            values
            (101,'Rahul',45000.45,'Male');
           '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data Inserted successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()