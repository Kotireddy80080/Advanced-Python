print("Inheritance")
print("3.Multiple Inheritance")   #"more than one parent class to one child class"
import time 
class A_class:
    def m1(self):
        print("A_class ....")
class B_class:
    def m2(self):
        print("B_class ...")
class C_class:
    def m3(self):
        print("C_class ...")
class D_class:
    def m4(self):
        print("D_class ...")
class S1_class(A_class,B_class,C_class,D_class):
    def m5(self):
        print("S1_class ...")
s1=S1_class()
s1.m1()
s1.m2()
s1.m3()
s1.m4()
s1.m5()
print()
time.sleep(3)
print("End of an application")

print("example-1")
import time 
class I_HUB_1:
    def m1(self):
        print("This is Service_One")
class I_HUB_2:
    def m1(self):
        print("This is Service_Two")
class I_HUB_3:
    def m1(self):
        print("This is Service_Three")
class I_HUB_4:
    def m1(self):
        print("This is Service_Four")
class I_HUB_5(I_HUB_1,I_HUB_2,I_HUB_3,I_HUB_4):
    def m1(self):
        print("This is Service_Five")
i1=I_HUB_5()
i1.m1()
print()
time.sleep(3)
print("End of an application")


print("example-2")
import time 
class I_HUB_1:
    def m1(self):
        print("This is Service_One")
class I_HUB_2:
    def m1(self):
        print("This is Service_Two")
class I_HUB_3:
    def m1(self):
        print("This is Service_Three")
class I_HUB_4:
    def m1(self):
        print("This is Service_Four")
class I_HUB_5(I_HUB_1,I_HUB_2,I_HUB_3,I_HUB_4):pass
i1=I_HUB_5()
i1.m1()
print()
time.sleep(3)
print("End of an application")

print("example-3")
import time 
class I_HUB_1:pass
   
class I_HUB_2:
    def m1(self):
        print("This is Service_Two")
class I_HUB_3:
    def m1(self):
        print("This is Service_Three")
class I_HUB_4:
    def m1(self):
        print("This is Service_Four")
class I_HUB_5(I_HUB_1,I_HUB_2,I_HUB_3,I_HUB_4):pass
i1=I_HUB_5()
i1.m1()
print()
time.sleep(3)
print("End of an application")

print("example-4")
import time 
class I_HUB_1:pass
class I_HUB_2:pass
class I_HUB_3:
    def m1(self):
        print("This is Service_Three")
class I_HUB_4:
    def m1(self):
        print("This is Service_Four")
class I_HUB_5(I_HUB_1,I_HUB_2,I_HUB_3,I_HUB_4):pass
i1=I_HUB_5()
i1.m1()
print()
time.sleep(3)
print("End of an application")

print("example-5")
import time 
class I_HUB_1:pass
class I_HUB_2:pass
class I_HUB_3:pass     
class I_HUB_4:pass
class I_HUB_5(I_HUB_1,I_HUB_2,I_HUB_3,I_HUB_4):pass
i1=I_HUB_5()
print()
time.sleep(3)
print("End of an application")

