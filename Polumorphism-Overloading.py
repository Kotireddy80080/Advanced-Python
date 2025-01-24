print("1.Overloding")
print("a.An operator  overloading")

print("example-1")
class product_class:
    def __init__(self,items):
        self.items=items
p1=product_class(190)
print(p1)
print()

print("example-2")
class product_class:
    def __init__(self,items):
        self.items=items
    def __str__(self):
        return "number of items in p1:"+str(self.items)
p1=product_class(190)
print(p1)
print()

print("example-3")
class Product_Class:
    def __init__(self,items):
        self.items=items 
    def __str__(self):
        return str(self.items)
p1=Product_Class(190)
print("Number of items in P1 is:",p1)
print()


print("example-4")  #"more than two numbers use this method"
class Product_Class:
    def __init__(self,items):
        self.items=items 
    def __str__(self):
        return str(self.items)
    def __add__(self,other):
        obj1=self.items+other.items 
        P1=Product_Class(obj1)
        return P1
p1=Product_Class(190)
print("Number of items in P1 is:",p1)
print()
p2=Product_Class(19)
print("Number of items in P2 is:",p2)
print()
p3=Product_Class(1000)
print("Number of items in P2 is:",p3)
print()
p4=Product_Class(575)
print("Number of items in P2 is:",p4)
print()
p5=Product_Class(2100)
print("Number of items in P2 is:",p5)
print()
print("The result_set is:",p1+p2+p3+p4+p5)
print()


print("example-5")
class Product_Class:
    def __init__(self,items):
        self.items=items 
    def __str__(self):
        return str(self.items)
    def __iadd__(self,other):
        return self.items+other.items
        
p1=Product_Class(190)
print("Number of items in P1 is:",p1)
print()
p2=Product_Class(19)
p1+=p2
print("The result_set is:",p1)
print()


print("Method overloading")  # "method overloading not supported then we can use default and variable length argument"
print("Method Overloading using default argument")
class I_HUB_1:
    def m1(self,X1=None,X2=None,X3=None):
        if(X1!=None and X2!=None and X3!=None):
            print("Sum of three numbers are:",X1+X2+X3)
        elif(X1!=None and X2!=None):
            print("Sum of two numbers are:",X1+X2)
        else:
            print("Only three or two number of arguments")
i1=I_HUB_1()
i1.m1(100,200,300)
print()
i1.m1(100,200)
print()
i1.m1(1000)
print()


print("Method Overloading using Variable length argument")
print("Example-1")
class I_HUB_1:
    def m1(self,*obj1):
        print(obj1)
i1=I_HUB_1()
i1.m1()
print()
i1.m1(1000)
print()
i1.m1(1000,2000)
print()
i1.m1(1000,2000,3000)
print()
i1.m1(1000,2000,3000,4000)
print()
i1.m1(1000,2000,3000,4000,5000)
print()

print("Example-2") # "fetch"
class I_HUB_1:
    def m1(self,*obj1):
        for x1 in obj1:
            print(x1)
i1=I_HUB_1()
i1.m1()
print()
i1.m1(1000)
print()
i1.m1(1000,2000)
print()
i1.m1(1000,2000,3000)
print()
i1.m1(1000,2000,3000,4000)
print()
i1.m1(1000,2000,3000,4000,5000)
print()

print("Example-3")  #"sum"
class I_HUB_1:
    def m1(self,*obj1):
        S1=0 
        for x1 in obj1:
            S1=S1+x1 
        print("Sum is:",S1)
       
i1=I_HUB_1()
i1.m1()
print()
i1.m1(1000)
print()
i1.m1(1000,2000)
print()
i1.m1(1000,2000,3000)
print()
i1.m1(1000,2000,3000,4000)
print()
i1.m1(1000,2000,3000,4000,5000)
print()

print("Constructor overloading")  # "Constructor overloading not supported then we can use default and variable length argument"
print("Constructor Overloading with Default argument")
class I_HUB_2:
    def __init__(self,X1=None,X2=None,X3=None):
        print("Constructor_Method/Function")
i1=I_HUB_2(10,20,30)
print()
i2=I_HUB_2(10,20)
print()
i3=I_HUB_2(10)
print()


print("Constructor overloading using Variable length argument")
class I_HUB_2:
    def __init__(self,*X1):
        print("Constructor_Method/Function")
i1=I_HUB_2()
print()
i2=I_HUB_2(100)
print()
i3=I_HUB_2(100,200)
print()
i4=I_HUB_2(100,200,300)
print()
i5=I_HUB_2(100,200,300,400)
print()