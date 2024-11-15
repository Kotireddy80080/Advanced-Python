print("Composition And Aggregation ")
import time 
class Product_Details:
    Company_Name="Samsung"   #static variable
    def __init__(self):      #instance variable
        self.Pid=1001 
        self.Pname="Mobile_1"
        self.Price=23000.0 
    def m1(self):
        print("Pid is:",self.Pid)
        print("Pname is:",self.Pname)
        print("Price is:",self.Price)
p1=Product_Details()
p1.m1()
print("company name is:",Product_Details.Company_Name)
print()
time.sleep(3)
print("End of an application")