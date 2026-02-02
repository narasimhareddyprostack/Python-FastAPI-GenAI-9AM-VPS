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
            update employee
            set ename='Priyanka Gandhi'
            where eid=103;
            '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data Updated Successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()