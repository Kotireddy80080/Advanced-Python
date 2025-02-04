print("Example-1")
import time 
import csv 
with open("ihub_1.csv","w",newline="") as f:
    obj1=csv.writer(f)
    obj1.writerow(["Pid","Pname","Price","Company","M_date","Exp_date"])
    n=eval(input("Enter the number of rows:"))
    for x1 in range(n):
        Pid=int(input("Enter the Pid:"))
        Pname=input("Enter the Pname:")
        Price=float(input("Enter the Price:"))
        Company=input("Enter the Company:")
        M_date=input("Enter the M_date_year:")
        Exp_date=input("Enter the Exp_date_year:")
        obj1.writerow([Pid,Pname,Price,Company,M_date,Exp_date])
    print("A csv file is created successfully ...")
print()
time.sleep(2)
print("End of an application")


print("Example-2")
import time 
import csv 
with open("ihub_1.csv","r",newline="") as f:
    obj1=csv.reader(f)
    print(obj1)
print()
time.sleep(2)
print("End of an application")


print("Example-3")
import time 
import csv 
with open("ihub_1.csv","r",newline="") as f:
    obj1=csv.reader(f)
    obj2=list(obj1)
    print(obj2)
   
print()
time.sleep(2)
print("End of an application")


print("Example-4")
import time 
import csv 
with open("ihub_1.csv","r",newline="") as f:
    obj1=csv.reader(f)
    obj2=list(obj1)
    for x1 in obj2:
        for x2 in x1:
            print(x2,end="  ")
        print()
print()
time.sleep(2)
print("End of an application")