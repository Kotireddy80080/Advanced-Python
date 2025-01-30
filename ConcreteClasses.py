from abc import *
class I_HUB_1(ABC):
    @abstractmethod 
    def m1(self):
        pass 
    @abstractmethod 
    def m2(self):
        pass 
    @abstractmethod 
    def m3(self):
        pass 
    @abstractmethod 
    def m4(self):
        pass 
class I_HUB_2(I_HUB_1):
    def m1(self):
        print("M1_service")
    def m2(self):
        print("M2_service")
    def m3(self):
        print("M4_service")
class I_HUB_3(I_HUB_2):
    def m4(self):
        print("M4_service")
i1=I_HUB_3()
i1.m1()
print()
i1.m2()
print()
i1.m3()
print()
i1.m4()
print()


print("why do we require concrete classes")
from abc import *
class I_HUB_1(ABC):
    @abstractmethod 
    def m1(self):
        pass 
    @abstractmethod 
    def m2(self):
        pass 
    @abstractmethod 
    def m3(self):
        pass 
    @abstractmethod 
    def m4(self):
        pass 
class I_HUB_2(I_HUB_1):
    def m1(self):
        print("M1_service")
    def m2(self):
        print("M2_service")
    def m3(self):
        print("M3_service")
    def m4(self):
        print("M4_Service")
i1=I_HUB_2()
i1.m1()
print()
i1.m2()
print()
i1.m3()
print()
i1.m4() 
print()

