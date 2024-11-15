print("Garbage collector And Destructot")
print("1.check it is useful object or not")
import time 
class I_HUB_APP_STORE:
    def __init__(self):
        print("Constructor_function/Constructor_Method")
i1=I_HUB_APP_STORE()
print()
time.sleep(3)
print("End of an application")


print("example-2")
import time 
class I_HUB_APP_STORE:
    def __init__(self):
        print("Constructor_function/Constructor_Method")
    def __del__(self):
        print("Destructor_Method:Cleaning Memory blocks...")
i1=I_HUB_APP_STORE()
print()
i1=None 
print()
time.sleep(5)
print("End of an application")


print("example-3")
import time 
class I_HUB_APP_STORE:
    def __init__(self):
        print("Constructor_function/Constructor_Method")
    def __del__(self):
        print("Destructor_Method:Cleaning Memory blocks...")
i1=I_HUB_APP_STORE()
print()
del i1
print()
time.sleep(5)
print("End of an application")


print("example-4")
import time 
class I_HUB_APP_STORE:
    def __init__(self):
        print("Constructor_function/Constructor_Method")
    def __del__(self):
        print("Destructor_Method:Cleaning Memory blocks...")
i1=I_HUB_APP_STORE()
i2=i1 
i3=i2 
i4=i3 
i5=i4 
i6=i5 
del i1 
time.sleep(2)
print("I1 reference gone but object is there ...")
print()
del i2
time.sleep(2)
print("I2 reference gone but object is there ...")
print()
del i3
time.sleep(2)
print("I3 reference gone but object is there ...")
print()
del i4
time.sleep(2)
print("I4 reference gone but object is there ...")
print()
del i5 
time.sleep(2)
print("I5 reference gone but object is there ...")
print()
del i6 
print()
time.sleep(5)
print("End of an application")


print("example-5")
import time 
class I_HUB_APP_STORE:
    def __init__(self):
        print("Constructor_function/Constructor_Method")
    def __del__(self):
        print("Destructor_Method:Cleaning Memory blocks...")
i1=I_HUB_APP_STORE()
i1=None
i2=i1 
i3=i2 
i4=i3 
i5=i4 
i6=i5 
del i1 
time.sleep(2)
print("I1 reference gone but object is there ...")
print()
del i2
time.sleep(2)
print("I2 reference gone but object is there ...")
print()
del i3
time.sleep(2)
print("I3 reference gone but object is there ...")
print()
del i4
time.sleep(2)
print("I4 reference gone but object is there ...")
print()
del i5 
time.sleep(2)
print("I5 reference gone but object is there ...")
print()
del i6 
print()
time.sleep(5)
print("End of an application")


print("example-6")
import time 
class I_HUB_APP_STORE:
    def __init__(self):
        print("Constructor_function/Constructor_Method")
    def __del__(self):
        print("Destructor_Method:Cleaning Memory blocks...")
i1=[I_HUB_APP_STORE(),I_HUB_APP_STORE(),I_HUB_APP_STORE(),I_HUB_APP_STORE(),I_HUB_APP_STORE()]
print()
i1=None 
print()
time.sleep(3)
print("End of an application")


print("example-7")
import time 
class I_HUB_APP_STORE:
    def __init__(self):
        print("Constructor_function/Constructor_Method")
    def __del__(self):
        print("Destructor_Method:Cleaning Memory blocks...")
i1=[I_HUB_APP_STORE(),I_HUB_APP_STORE(),I_HUB_APP_STORE(),I_HUB_APP_STORE(),I_HUB_APP_STORE()]
print()
del i1
print()
time.sleep(3)
print("End of an application")


