print("1.Instance Variable")   #by constrctor method
print("a.Defineing or Declareing")
class i_hub_app_store:
    def __init__(self):
        self.a1=1001
        self.a2=1002
        self.a3=1003
    def m1(self):
        self.b1=2001
        self.b2=2002
        self.b3=2003
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=i_hub_app_store()       #"using constrctor"
print(i1.__dict__)    
print()
i1.m1()                 #"Object reference variable"
print(i1.__dict__)
print()
i1.c1=3001
i1.c2=3002
i1.c3=3003
print(i1.__dict__)      #"outside object"
print()

print("b.accessing and printing")
print("1st way to access or print")
class i_hub_app_store:
    def __init__(self):
        self.a1=1001
        self.a2=1002
        self.a3=1003
        print(self.a1,self.a2,self.a3)
    def m1(self):
        self.b1=2001
        self.b2=2002
        self.b3=2003
        print(self.b1,self.b2,self.b3)
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=i_hub_app_store()    #"using constrctor"
print()
i1.m1()                 #"Object reference variable"
print()
i1.c1=3001
i1.c2=3002
i1.c3=3003
print(i1.c1,i1.c2,i1.c3)   #"outside class"
print()

print("2st way to access or print")
class i_hub_app_store:
    def __init__(self):
        self.a1=1001
        self.a2=1002
        self.a3=1003
    def m1(self):
        print(self.a1,self.a2,self.a3)
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=i_hub_app_store()    #"using constrctor"
print()
i1.m1()                 #"Object reference variable"
print()

print("3st way to access or print")
class i_hub_app_store:
    def __init__(self):
        self.a1=1001
        self.a2=1002
        self.a3=1003
    def m1(self):
        pass
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=i_hub_app_store()   
print()               
print(i1.a1,i1.a2,i1.a3)  #"otside of class"
print()

print("c.deleting ")
class i_hub_app_store:
    def __init__(self):
        self.a1=1001
        self.a2=1002
        self.a3=1003
        del self.a1,self.a3
    def m1(self):
        self.b1=2001
        self.b2=2002
        self.b3=2003
        del self.b1,self.b2 
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=i_hub_app_store()       #"using constrctor"
print(i1.__dict__)    
print()
i1.m1()                 #"Object reference variable"
print(i1.__dict__)
print()
i1.c1=3001
i1.c2=3002
i1.c3=3003
del i1.c2
print(i1.__dict__)      #"outside object"
print()

print("d.updateing")
class i_hub_app_store:
    def __init__(self):
        self.pid=1001
    def m1(self):
        self.pid=2001
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=i_hub_app_store()    #"using constrctor"
print()
i1.m1()                #"Object reference variable"
print()
i1.pid=3001
print(i1.pid)
print()





