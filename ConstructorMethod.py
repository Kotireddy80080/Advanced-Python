print("1.Constructor method or function ")
print("a.By Default constructor")
class i_hub_1:
    def __init__(self):
        print("constructor method or function")
i1=i_hub_1()
print()


print("b.By Changeing the Constructor")
class i_hub_1:
    def __init__(x1):
        print("constructor method or function")
i1=i_hub_1()
print()


print("c.More than one object in a constructor")
class i_hub_1:
    def __init__(self):
        print("constructor method or function")
i1=i_hub_1()
print()
i2=i_hub_1()
print()
i3=i_hub_1()
print()



print("Example-1:Basic Constructor")
class i_hub_1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name:{self.name},age:{self.age}")
i1=i_hub_1("koti",25)
i1.display()
print()

print("Example-2:default Constructor")
class car:
    def __inti__(self,brand="toyota",model="corolla"):
        self.brand=brand
        self.model=model
    def m1(self):
        print(f"car:{self.brand},{self.model}")
car1=car()
car.m1()
print()

