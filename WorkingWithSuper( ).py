print("Example on super class")

class Person_Class:
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
    def m1(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
class Employee_Class(Person_Class):
    def __init__(self,name,age,eid,esal,design,company):
        super().__init__(name,age)
        self.eid=eid 
        self.esal=esal 
        self.design=design 
        self.company=company 
    def m2(self):
        super().m1()
        print("Eid is:",self.eid)
        print("Esal is:",self.esal)
        print("Design is:",self.design)
        print("Company is:",self.company)
class Customer_Class(Person_Class):
    def __init__(self,name,age,cid,address,city,mobile_number):
        super().__init__(name,age)
        self.cid=cid 
        self.address=address 
        self.city=city 
        self.mobile_number=mobile_number
    def m3(self):
        super().m1()
        print("Cid is:",self.cid)
        print("Address is:",self.address)
        print("City is:",self.city)
        print("Mobile_number is:",self.mobile_number)
e1=Employee_Class("Jessica_1",26,1001,49000.0,"Python Developer","HCL")
e1.m2()
print()
c1=Customer_Class("Rahul_1",23,1007,"Mumbai","Bandra","+91-7654123412")
c1.m3()
print()


print("can we access all four methods by using constructor method by super keyword")

class I_HUB_IT_SERVICES:
    def __init__(self):
        print("Full Stack Python Developer")
    def m1(self):
        print("Python Developer")
    @classmethod 
    def m2(cls):
        print("Data Engineer")
    @staticmethod 
    def m3():
        print("Angular/React Developer")
class I_HUB_APP_STORE(I_HUB_IT_SERVICES):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
i1=I_HUB_APP_STORE()
print()

print("can we access all four methods by using instance  method by super keyword")

class I_HUB_IT_SERVICES:
    def __init__(self):
        print("Full Stack Python Developer")
    def m1(self):
        print("Python Developer")
    @classmethod 
    def m2(cls):
        print("Data Engineer")
    @staticmethod 
    def m3():
        print("Angular/React Developer")
class I_HUB_APP_STORE(I_HUB_IT_SERVICES):
    def S1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3() 
i1=I_HUB_APP_STORE()
i1.S1()
print()

print("we cannot access all four methods by using classmethod and static method  method by super keyword")

class I_HUB_1:
    def m1(self):
        print("This is service_one")
class I_HUB_2(I_HUB_1):
    def m1(self):
        print("This is service_two")
class I_HUB_3(I_HUB_2):
    def m1(self):
        print("This is service_three")
class I_HUB_4(I_HUB_3):
    def m1(self):
        print("This is service_four")
class I_HUB_5(I_HUB_4):
    def m1(self):
        I_HUB_1.m1(self)
i1=I_HUB_5()
i1.m1()
print()

