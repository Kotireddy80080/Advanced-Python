print("write")
print("Example-1")
import time 
f2=open("ihub_1.txt","w")
f2.write("ABC")
f2.write("abc")
f2.write("123")
print()
print("New file is created successfully")
print()
f2.close()
print()
print("End of an application")

print("Example-2")
import time 
f2=open("ihub_1.txt","w")
f2.write("ABC\n")
f2.write("abc\n")
f2.write("123\n")
print()
print("New file is created successfully")
print()
f2.close()
print()
print("End of an application")


print("Example-3")
import time 
f2=open("ihub_1.txt","a")
f2.write("ABC\n")
f2.write("abc\n")
f2.write("_@$\n")
print()
print("New file is created successfully")
print()
f2.close()
print()
print("End of an application")



print("writelines")
print("Example-1")
import time 
f1=open("ihub_3.txt","w")
L1=["1001\n","Jessica_1\n","39000.0\n","Developer_1\n","HCL\n"]
f1.writelines(L1)
print("A new file is created successfully ...")
print()
f1.close()
print()
time.sleep(2)
print("End of an application")

print("Example-2")
import time 
f1=open("ihub_3.txt","w")
L1=["1001\n","Jessica_1\n","39000.0\n","Developer_1\n","HCL\n"]
L2=["1002\n","Jessica_2\n","41000.0\n","Developer_2\n","HCL\n"]
L3=["1003\n","Jessica_3\n","42000.0\n","Developer_3\n","HCL\n"]
L4=["1004\n","Jessica_4\n","43000.0\n","Developer_4\n","HCL\n"]
f1.writelines(L1)
f1.writelines(L2)
f1.writelines(L3)
f1.writelines(L4)
print("A new file is created successfully ...")
print()
f1.close()
print()
time.sleep(2)
print("End of an application")


print("file to console or application")
print("Example-1")
import time 
f1=open("ihub_3.txt","r")
X1=f1.read()
print("**********************")
print("File_Name is:",f1.name)
print()
print("***********************")
print(X1)
print()
f1.close()
print()
time.sleep(2)
print("End of an application")


print("Example-2")
import time 
f1=open("ihub_3.txt","r")
X1=f1.read(17)
print("**********************")
print("File_Name is:",f1.name)
print()
print("***********************")
print(X1)
print()
f1.close()
print()
time.sleep(2)
print("End of an application")


print("Example-3")
import time 
f1=open("ihub_3.txt","r")
X1=f1.readline()
print("**********************")
print("File_Name is:",f1.name)
print()
print("***********************")
print(X1)
print()
f1.close()
print()
time.sleep(2)
print("End of an application")


print("Example-4")
import time 
f1=open("ihub_3.txt","r")
X1=f1.readlines()
print("**********************")
print("File_Name is:",f1.name)
print()
print("***********************")
print(X1)
print()
f1.close()
print()
time.sleep(2)
print("End of an application")


print("Example-5")
import time 
f1=open("ihub_3.txt","r")
X1=f1.readlines()
print("**********************")
print("File_Name is:",f1.name)
print()
print("***********************")
for x1 in X1:
    print(x1,end=" ")
print()
f1.close()
print()
time.sleep(2)
print("End of an application")

print("Example-6")
import time 
f1=open("ihub_3.txt","r")
for x1 in f1:
    print(x1)
print()
f1.close()
print()
time.sleep(3)
print('End of an application')



print("tell()")

import time 
f1=open("ihub_1.txt","r")
obj1=f1.tell()
print("Current_File_Pointer_Position is:",obj1)
print()
obj2=f1.read(15)
print(obj2)
print()
obj3=f1.tell()
print("Current_File_Pointer_Position is:",obj3)
print()
f1.close()
print()
time.sleep(2)
print("End of an application")


print("seek()")
f1=open("ihub_1.txt","r")
obj1=f1.tell()
print("Current_File_Pointer_Position is:",obj1)
print()
obj2=f1.read(15)
print(obj2)
print()
obj3=f1.tell()
print("Current_File_Pointer_Position is:",obj3)
print()
obj4=f1.seek(0)
print("Current_File_Pointer_Position is:",obj4)
print()
obj5=f1.read(15)
print(obj5)
print()
obj6=f1.tell()
print("Current_File_Pointer_Position is:",obj6)
print()
f1.close()
print()
time.sleep(2)
print("End of an application")