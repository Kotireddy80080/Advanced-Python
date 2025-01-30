print("Access modifiers")
print("public,protected,private")
class I_HUB_APP_STORE:
    Pid=1001 
    _Pname="Mobile_1"
    __Price=29000 
    def __ini__(self):
        pass 
    def m1(self):
        print("Pid is:",I_HUB_APP_STORE.Pid)
        print()
        print("Pname is:",I_HUB_APP_STORE._Pname)
        print()
        print("Price is:",I_HUB_APP_STORE.__Price)
i1=I_HUB_APP_STORE()
i1.m1()
print()
print("Pid is:",I_HUB_APP_STORE.Pid)
print()
print("Pname is:",I_HUB_APP_STORE._Pname)
print()
print("Price is:",I_HUB_APP_STORE.__Price)
print()
