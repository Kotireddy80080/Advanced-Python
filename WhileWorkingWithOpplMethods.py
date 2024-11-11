print("1.Constructor method or function ")
print("a.By Default constructor")
import time
class i_hub_1:
    def __init__(self):
        print("constructor method or function")
i1=i_hub_1()
print()
time.sleep(2)
print("end of an application")

print("b.By Changeing the Constructor")
import time
class i_hub_1:
    def __init__(x1):
        print("constructor method or function")
i1=i_hub_1()
print()
time.sleep(2)
print("end of an application")

print("c.More than one object in a constructor")
import time
class i_hub_1:
    def __init__(self):
        print("constructor method or function")
i1=i_hub_1()
print()
i2=i_hub_1()
print()
i3=i_hub_1()
print()
time.sleep(2)
print("end of an application")

print("2.Instance method or function")
print("a.example")
import time
class i_hub_2:
    def m1(self):
        print("instance method or function")
i1=i_hub_2()
i1.m1()   # (Object reference variable)
print()
time.sleep(2)
print("end of an application")

print("b.By Changeing the self")
import time
class i_hub_2:
    def m1(x1):
        print("instance method or function")
i1=i_hub_2()
i1.m1()   # (Object reference variable)
print()
time.sleep(2)
print("end of an application")

print("3.Class Method")
class i_hub_3:
    @classmethod
    def m3(cls):
        print("class method")
i1=i_hub_3()
i1.m3()
print()       #("using class name")
i_hub_3.m3()  #("using object reference variable")
print()

print("4.static method")
class i_hub_3:
    @staticmethod
    def m3():
        print("static method")
i1=i_hub_3()
i1.m3()
print()       #("using class name")
i_hub_3.m3()  #("using object reference variable")
print()

print("a.adding by using static method")
class i_hub_3:
    @staticmethod
    def m3(x1,x2):
        print("sum of:",x1+x2)
i1=i_hub_3()
i1.m3(1000,2000)
print()       #("using class name")
i_hub_3.m3(2000,3000)  #("using object reference variable")
print()
 
print("Based on the Opps Methods examples-1")
class i_hub_it_services:
    def __init__(self):
        self.eid=101
        self.ename="koti"
        self.esal=25000
        self.company="hcl"
    def s1(self):
        print("eid is:",self.eid)
        print("ename is:",self.ename)
        print("esal is:",self.esal)
        print("company is:",self.company)
i1=i_hub_it_services()
i1.s1()
print()

print("Based on the Opps Methods examples-2")
class i_hub_it_services:
    def __init__(self,eid,ename,esal,company):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.company=company
    def s1(self):
        print("eid is:",self.eid)
        print("ename is:",self.ename)
        print("esal is:",self.esal)
        print("company is:",self.company)
i1=i_hub_it_services(1001,"koti",25000,"hcl")
i1.s1()
print()

 
print("Based on the Opps Methods examples-3:adding more objects")
class i_hub_it_services:
    def __init__(self,eid,ename,esal,company):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.company=company
    def s1(self):
        print("eid is:",self.eid)
        print("ename is:",self.ename)
        print("esal is:",self.esal)
        print("company is:",self.company)
i1=i_hub_it_services(1001,"koti",25000,"hcl")
i1.s1()
print()
i2=i_hub_it_services(1002,"koti",27000,"hcl")
i2.s1()
print()
i3=i_hub_it_services(1003,"koti",29000,"hcl")
i3.s1()
print()


print("Based on the Opps Methods examples-4")
class i_hub_it_services:
    def __init__(self):
        self.eid=int(input("enter the eid:"))
        self.ename=input("enter the ename:")
        self.esal=float(input("enter the esal:"))
        self.company=input("enter the company")
    def s1(self):
        print(self.eid,self.ename,self.esal,self.company)
i1=i_hub_it_services()
i1.s1()
print()

print("Based on the Opps Methods examples-5")
class i_hub_it_services:
    def __init__(self,eid,ename,esal,company):
        self.eid=int(input("enter the eid:"))
        self.ename=input("enter the ename:")
        self.esal=float(input("enter the esal:"))
        self.company=input("enter the company")
    def s1(self):
        print(self.eid,self.ename,self.esal,self.company)
i1=i_hub_it_services(eid=None,ename=None,esal=None,company=None)
i1.s1()
print()

