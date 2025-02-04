print("1.How to create a Database")
import time 
import mysql.connector 
try:
    sql_1="create database my_database_101"
    con=mysql.connector.connect(host="localhost",user="root",password="")
    cursor=con.cursor()
    cursor.execute(sql_1)
    print("Databse is created successfully ...")
except mysql.connector.DatabaseError as e: 
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if con:
        con.close()
    elif cursor:
        cursor.close()
print()
time.sleep(3)
print("End of an applicaton")


print("2.how to create table")
import time 
import mysql.connector 
try:
    sql_1="create table Products(Pid INT,Pname VARCHAR(20),Price INT)"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute(sql_1)
    print("Table is created successfully ...")
except mysql.connector.DatabaseError as e: 
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if con:
        con.close()
    elif cursor:
        cursor.close()
print()
time.sleep(3)
print("End of an applicaton")


print("3.How to add additional colums into table")
import time 
import mysql.connector 
try:
    sql_1="alter table products add company varchar(50)"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute(sql_1)
    print("Table is created successfully ...")
except mysql.connector.DatabaseError as e: 
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if con:
        con.close()
    elif cursor:
        cursor.close()
print()
time.sleep(3)
print("End of an applicaton")


print("4.How to change table name")
import time 
import mysql.connector 
try:
    sql_1="alter table products rename as p1"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute(sql_1)
    print("Table is created successfully ...")
except mysql.connector.DatabaseError as e: 
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if con:
        con.close()
    elif cursor:
        cursor.close()
print()
time.sleep(3)
print("End of an applicaton")

print("5.How to insert records into table")
import time 
import mysql.connector 
try:
    sql_1="insert into P1 values(1001,'Mobile_1',23000.0,'Samsung')"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute(sql_1)
    con.commit()
    print("A record is inserted successfully ...")
except mysql.connector.DatabaseError as e: 
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if con:
        con.close()
    elif cursor:
        cursor.close()
print()
time.sleep(3)
print("End of an applicaton")

print("6.Insert more than one record")
import time 
import mysql.connector 
try:
    sql_1="insert into P1 values(%s,%s,%s,%s)"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    record=([1002,"Mobile_2",27000,"Samsung"],[1003,"Mobile_3",28000,"Samsung"])
    cursor.executemany(sql_1,record)
    con.commit()
    print("A record is inserted successfully ...")
except mysql.connector.DatabaseError as e: 
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if con:
        con.close()
    elif cursor:
        cursor.close()
print()
time.sleep(3)
print("End of an applicaton")


print("7.how to insert data using for loop")
import time 
import mysql.connector 
try:
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    n=eval(input("Enter the number of rows:"))
    for x1 in range(n):
        Pid=int(input("Enter the Pid:"))
        Pname=input("Enter the Pname:")
        Price=float(input("Enter the Price:"))
        Company=input("Enter the Company:")
        sql="insert into p1 values(%s,'%s',%s,'%s')"
        cursor.execute(sql%(Pid,Pname,Price,Company))
        con.commit()
    print("Records are inserted successfully ..")
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")

print("8.how to insert data using while loop")
import time 
import mysql.connector 
try:
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    while True:
        Pid=int(input("Enter the Pid:"))
        Pname=input("Enter the Pname:")
        Price=float(input("Enter the Price:"))
        Company=input("Enter the Company")
        sql="insert into p1 values(%s,'%s',%s,'%s')"
        cursor.execute(sql%(Pid,Pname,Price,Company))
        option=input("Enter the option [YES|NO]:")
        if(option=="NO"):
            con.commit()
            break
  
 
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")


print("9.To fetch the data")
print("Example-1")   #using for loop
import time 
import mysql.connector 
try:
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute("select * from p1")
    data=cursor.fetchall()
    print("----Product_Information-----")
    for x1 in data:
        print("Pid is:",x1[0])
        print("Pname is:",x1[1])
        print("Price is:",x1[2])
        print("Company is:",x1[3])
        print()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")

print("Example-2")   # using nested while loop
import time 
import mysql.connector 
try:
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute("select * from p1")
    data=cursor.fetchall()
    print("----Product_Information-----")
    for x1 in data:
        for x2 in x1:
            print(x2,end="  ")
        print()    
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")


print("10.Delete the records in a table")
import time 
import mysql.connector 
try:
    sql="delete from p1 where Pid=1005"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute(sql)
    con.commit()
    print("Records are removed successfully ...")
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")

print("11.Update the records in a table")
import time 
import mysql.connector 
try:
    sql="update P1 set Price=Price+10000 where Pid=1001"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute(sql)
    con.commit()
    print("Record is udpated successfully ...")
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")

print("12.Deleting the data/information from the database")
import time 
import mysql.connector 
try:
    sql="truncate table p1"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute(sql)
    print("Records are deleted succssfully ....")
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")

print("13.Deleting the table")
import time 
import mysql.connector 
try:
    sql="drop table p1"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute(sql)
    print("table is deleted successfully ....")
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")

print("14.Delete the database")
import time 
import mysql.connector 
try:
    sql="drop database my_database_101"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="my_database_101")
    cursor=con.cursor()
    cursor.execute(sql)
    print("Database is deleted successfully ....")
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")