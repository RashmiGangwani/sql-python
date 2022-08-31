import mysql.connector as connection

mydb=connection.connect(host="localhost",user="root",passwd="Asdfghjkl$1")
#print(mydb)
cursor = mydb.cursor()
#cursor.execute("create database rashmi")

#cursor.execute("create table rashmi.ineuron(employee_id int(10), emp_name varchar(80),emp_emailid varchar(60),emp_salary int(6),emp_attendance int(3))")
s="insert into rashmi.ineuron values(101, 'sudhanshu', 'sudhanshu@ineuron.ai', 100,30)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)



mydb.commit()
cursor.execute("select * from rashmi.ineuron")
for i in cursor.fetchall():
    print(i)