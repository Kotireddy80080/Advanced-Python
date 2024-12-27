print("2.Instance method or function")
print("a.example")

class i_hub_2:
    def m1(self):
        print("instance method or function")
i1=i_hub_2()
i1.m1()   # (Object reference variable)
print()


print("b.By Changeing the self")

class i_hub_2:
    def m1(x1):
        print("instance method or function")
i1=i_hub_2()
i1.m1()   # (Object reference variable)
print()

print("example-1")
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def m1(self,amount):
        self.salary+=amount
        print(f"{self.name}.new salary:{self.salary}")
emp=employee("john",50000)
emp.m1(5000)
print()




