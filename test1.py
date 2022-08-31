import mysql.connector as connection

mydb=connection.connect(host="localhost",user="root",passwd="Asdfghjkl$1")
cursor = mydb.cursor()
cursor.execute("select employee_id, emp_emailid from rashmi.ineuron")
l=[]
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))