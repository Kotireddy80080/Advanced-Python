print("4.static method")
class i_hub_3:
    @staticmethod
    def m3():
        print("static method")
i1=i_hub_3()
i1.m3()
print()       #("using class name")
i_hub_3.m3()  #("using object reference variable")
print()

print("Example-1")
class i_hub_3:
    @staticmethod
    def m3(x1,x2):
        print("sum of:",x1+x2)
i1=i_hub_3()
i1.m3(1000,2000)
print()       #("using class name")
i_hub_3.m3(2000,3000)  #("using object reference variable")
print()