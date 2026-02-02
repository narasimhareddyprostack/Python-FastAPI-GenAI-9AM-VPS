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
            (102,'Sonia',55000.45,'Female'),
            (103,'Priya',65000.45,'Female'),
            (104,'Modi',75000.45,'Male'),
            (105,'Amith',85000.45,'Male');

           '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data Inserted successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()