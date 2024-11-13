print("Static Variable")    #by class name
print("a.Defineing or Declareing")
class i_Hub_1:
    def __init__(self):
        i_Hub_1.a1=1001
        i_Hub_1.a2=1002
        i_Hub_1.a3=1003
        i_Hub_1.a4=1004
    def m1(self):
        i_Hub_1.b1=2001
        i_Hub_1.b2=2002
        i_Hub_1.b3=2003
    @classmethod
    def m2(cls):
        i_Hub_1.c1=3001
        i_Hub_1.c2=3002
        i_Hub_1.c3=3003
        i_Hub_1.c4=3004
    @staticmethod
    def m3():
        i_Hub_1.d1=4001
        i_Hub_1.d2=4002
        i_Hub_1.d3=4003
        i_Hub_1.d4=4004
i1=i_Hub_1()      
print(i_Hub_1.__dict__)    
print()
i1.m1()                 
print(i_Hub_1.__dict__)
print()
i1.m2()
print(i_Hub_1.__dict__)
print()
i1.m3()
print(i_Hub_1.__dict__)
print()
i_Hub_1.e1=5001
i_Hub_1.e1=5002
i_Hub_1.e1=5003
print(i_Hub_1.__dict__)     
print()

print("b.printing and accessing")
class I_HUB_1:
    def __init__(self):
        I_HUB_1.A1=101 
        I_HUB_1.A2=102 
        I_HUB_1.A3=103 
        I_HUB_1.A4=104 
        print(I_HUB_1.A1,I_HUB_1.A2,I_HUB_1.A3,I_HUB_1.A4)
    def m1(self):
        I_HUB_1.B1=201 
        I_HUB_1.B2=202 
        I_HUB_1.B3=203 
        I_HUB_1.B4=204
        print(I_HUB_1.B1,I_HUB_1.B2,I_HUB_1.B3,I_HUB_1.B4)
    @classmethod 
    def m2(cls):
        I_HUB_1.C1=301 
        I_HUB_1.C2=302 
        cls.C3=303 
        cls.C4=304
        print(I_HUB_1.C1,I_HUB_1.C2,cls.C3,cls.C4)
    @staticmethod 
    def m3():
        I_HUB_1.D1=501 
        I_HUB_1.D2=502 
        I_HUB_1.D3=503 
        I_HUB_1.D4=504
        print(I_HUB_1.D1,I_HUB_1.D2,I_HUB_1.D3,I_HUB_1.D4)
i1=I_HUB_1()
print()
i1.m1()
print()
i1.m2()
print()
i1.m3()
I_HUB_1.E1=701 
I_HUB_1.E2=702 
I_HUB_1.E3=703 
print()
print(I_HUB_1.E1,I_HUB_1.E2,I_HUB_1.E3)
print()

print("Deleteing a static variable")
class I_HUB_1:
    def __init__(self):
        I_HUB_1.A1=101 
        I_HUB_1.A2=102 
        I_HUB_1.A3=103 
        I_HUB_1.A4=104 
        del I_HUB_1.A1,I_HUB_1.A2
    def m1(self):
        I_HUB_1.B1=201 
        I_HUB_1.B2=202 
        I_HUB_1.B3=203 
        I_HUB_1.B4=204
        del I_HUB_1.B1,I_HUB_1.B2,I_HUB_1.B3
    @classmethod 
    def m2(cls):
        I_HUB_1.C1=301 
        I_HUB_1.C2=302 
        cls.C3=303 
        cls.C4=304
        del cls.C4,cls.C3
       
    @staticmethod 
    def m3():
        I_HUB_1.D1=501 
        I_HUB_1.D2=502 
        I_HUB_1.D3=503 
        I_HUB_1.D4=504
        del I_HUB_1.D1,I_HUB_1.D2,I_HUB_1.D3
        
i1=I_HUB_1()
print(I_HUB_1.__dict__)
print()
i1.m1()
print(I_HUB_1.__dict__)
print()
i1.m2()
print(I_HUB_1.__dict__)
print()
i1.m3()
print(I_HUB_1.__dict__)
print()
I_HUB_1.E1=701 
I_HUB_1.E2=702 
I_HUB_1.E3=703 
del I_HUB_1.E1,I_HUB_1.E2 
print(I_HUB_1.__dict__)
print()

print("updateing a static variable")
class I_HUB_1:
    Eid=1001 
    def __init__(self):
        I_HUB_1.Eid=1002 
    def m1(self):
        I_HUB_1.Eid=1003 
    @classmethod 
    def m2(cls):
        cls.Eid=1004 
    @staticmethod 
    def m3():
        I_HUB_1.Eid=1005
i1=I_HUB_1()
i1.m1()
print()
i1.m2()
print()
i1.m3()
print()
I_HUB_1.Eid=1006 
print("Eid is:",I_HUB_1.Eid)
print()
