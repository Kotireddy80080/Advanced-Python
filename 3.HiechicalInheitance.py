print("Inheritance")
print("3.Hiechical Inheritance")   #"one parent class to more then one child class"
import time 
class Father_Class:
    def m1(self):
        print("This is Father_Class ...")
class Son1_Class(Father_Class):
    def m2(self):
        print("This is Son1_Class ...")
class Son2_Class(Father_Class):
    def m3(self):
        print("This is Son2_Class ...")
class Son3_Class(Father_Class):
    def m4(self):
        print("This is Son_3 class ...")
f1=Father_Class()
f1.m1()
print()
s1=Son1_Class()
s1.m1()
s1.m2()
print()
s2=Son2_Class()
s2.m1()
s2.m3()
print()
s3=Son3_Class()
s3.m1()
s3.m4()
print()
time.sleep(3)
print("End of an application")