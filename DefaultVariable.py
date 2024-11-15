print("d.Default Variable")
print("example -1")
import time 
class Student_Clas:
    def __init__(self,Sid,Sname,Subject,Marks):
        self.Sid=Sid 
        self.Sname=Sname 
        self.Subject=Subject 
        self.Marks=Marks 
    def m1(self):
        print(self.Sid,self.Sname,self.Subject,self.Marks)
s1=Student_Clas(1001,"Jessica_1","JavaScript & Python",79)
s1.m1()
print()
time.sleep(3)
print("End of an application")

print("example -2")
import time 
class Operations_Class:
    def __init__(self,x1,x2):
        self.x1=x1 
        self.x2=x2 
        print(self.x1+self.x2)
o1=Operations_Class(100,200)
print()
time.sleep(2)
print("End of an application")

print("example -3")
import time 
class Operations_Class:
    def __init__(self,x1,x2):
        self.x1=x1 
        self.x2=x2 
    def m1(self):
        print("Sum is:",self.x1+self.x2)
o1=Operations_Class(101,102)
o1.m1()
print()
time.sleep(3)
print("End of an application")

print("example -4")
import time 
class Operations_Class:
    def __init__(self,x1,x2):
        self.x1=x1 
        self.x2=x2 
    def m1(self):
        return self.x1+self.x2
       
o1=Operations_Class(101,102)
print("Sum is:",o1.m1())
print()
time.sleep(3)
print("End of an application")
