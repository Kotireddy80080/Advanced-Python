print("example - 1")
import time 
class Car_Class:
    print("Car_class Implementation ...")
    class Engine_Class:
        print("Engine_class Implementation ...")
        def m1(self):
            print("This is First_Service ...")
c1=Car_Class()
e1=c1.Engine_Class()
e1.m1()
print()
time.sleep(3)
print("End of an application")

print("example - 2")
import time 
class Car_Class:
    print("Car_class Implementation ...")
    class Engine_Class:
        print("Engine_class Implementation ...")
        def m1(self):
            print("This is First_Service ...")
c1=Car_Class().Engine_Class().m1()
print()
time.sleep(2)
print("End of an application")

print("example -3")
import time 
class Language_Details:
    def __init__(self):
        self.name="Python Programming Language"
        self.doj=self.DOJ()
    def m1(self):
        print("Name of the language is:",self.name)
        print()
        self.doj.m2()
    class DOJ:
        def __init__(self):
            self.day=16 
            self.month=7 
            self.year=1989 
        def m2(self):
            print("Date of release is:{}/{}/{}".format(self.day,self.month,self.year))
l1=Language_Details()
l1.m1()
print()
time.sleep(2)
print("End of an application")

print("example -4")
import time 
class Univercity:
    print("Univercity_class Implementation ...")
    class College:
        print("College_class Implementation ...")
        def m1(self):
            print("1.AI with 4 years")
            print("2.DL with 4 years")
            print("3.ML with 4 years")
u1=Univercity()
c1=u1.College()
c1.m1()
print()
time.sleep(3)
print("End of an application")

print("example -5")
import time 
class Univercity:
    print("Univercity_class Implementation ...")
    class College:
        print("College_class Implementation ...")
        def m1(self):
            print("1.AI with 4 years")
            print("2.DL with 4 years")
            print("3.ML with 4 years")
u1=Univercity().College().m1()
print()
time.sleep(2)
print("End of an application")