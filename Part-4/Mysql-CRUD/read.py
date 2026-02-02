import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='9am')
    cursor=dbcon.cursor()
    sql_st='''   select * from employee; '''
    cursor.execute(sql_st)
    employees=cursor.fetchall()
    print(type(employees))
    for emp in employees:
        #print(emp)
        print(emp[1])

except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()