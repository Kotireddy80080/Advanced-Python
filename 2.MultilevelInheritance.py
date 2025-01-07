print("Inheritance")
print("2.Multilevel Inheritance")   #"one class to another class continously.."
print("Example -1")
import time 
class I_HUB_1:
    def m1(self):
        print("This is Service_One")
class I_HUB_2(I_HUB_1):
    def m2(self):
        print("This is Service_Two")
class I_HUB_3(I_HUB_2):
    def m3(self):
        print("This is Service_Three")
class I_HUB_4(I_HUB_3):
    def m4(self):
        print("This is Service_Four")
print()
i1=I_HUB_1()
i1.m1()
print()
i2=I_HUB_2()
i2.m1()
i2.m2()
print()
i3=I_HUB_3()
i3.m1()
i3.m2()
i3.m3()
print()
print()
i4=I_HUB_4()
i4.m1()
i4.m2()
i4.m3()
i4.m4()
print()
time.sleep(3)
print("End of an application")

print("Example -2")
import time 
class I_HUB_1:
    def m1(self):
        print("This is Service_One")
class I_HUB_2(I_HUB_1):
    def m2(self):
        print("This is Service_Two")
class I_HUB_3(I_HUB_2):
    def m3(self):
        print("This is Service_Three")
class I_HUB_4(I_HUB_3):
    def m4(self):
        print("This is Service_Four")
print()
i4=I_HUB_4()
i4.m1()
i4.m2()
i4.m3()
i4.m4()
print()
time.sleep(3)
print("End of an application")