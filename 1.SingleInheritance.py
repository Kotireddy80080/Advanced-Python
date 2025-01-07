print("Inheritance")
print("1.Single Inheritance")   #"one parent to one child"
import time 
class Quality_Thought:
    def m1(self):
        print("Quality_Thought is a Parent Software institute")
class I_HUB_1(Quality_Thought):
    def m2(self):
        print("IHUB_1 is a Child Software institute")
q1=Quality_Thought()
q1.m1()
print()
i1=I_HUB_1()
i1.m1()
print()
i1.m2()
print()
time.sleep(2)
print("End of an application")