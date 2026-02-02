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
            create table employee(
            eid int,
            ename varchar(32) not null,
            esal float,
            gender varchar(32) not null,
            primary key(eid)
            );
           '''
    cursor.execute(sql_st)
    print("New Table Created!")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()