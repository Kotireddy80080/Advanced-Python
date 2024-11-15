print("3.Local Variable")
class I_HUB_1:
    def __init__(self):
        A1=1001 
        A2=1002 
        A3=1003 
        print(A1,A2,A3)
    def m1(self):
        B1=2001 
        B2=2002 
        B3=2003 
        print(B1,B2,B3)
    @classmethod 
    def m2(cls):
        C1=3001 
        C2=3002 
        C3=3003 
        print(C1,C2,C3)
    @staticmethod 
    def m3():
        D1=4001 
        D2=4002
        D3=4003 
        print(D1,D2,D3)
i1=I_HUB_1()
i1.m1()
i1.m2()
i1.m3()
print()



