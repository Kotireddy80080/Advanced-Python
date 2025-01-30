print("Example-1")
import time 
from abc import * 
class I_HUB_1(ABC):
    pass 
i1=I_HUB_1()
print()
time.sleep(2)
print("End of an application")
print()

print("Example-2")
import time 
from abc import * 
class I_HUB_1(ABC):
    @abstractmethod 
    def m1(self):
        pass 
class I_HUB_2(I_HUB_1):
    def m1(self):
        print("This is ABS_Parent_Method ...")
i1=I_HUB_2()
i1.m1()
print()
time.sleep(3)
print("End of an application")
print()

print("Example-3")
import time 
from abc import * 
class I_HUB_1(ABC):
    @abstractmethod 
    def m1(self):
        pass 
class I_HUB_2(I_HUB_1):
    def m1(self):
        return "This ABS_method from IHUB_1_Class"
i1=I_HUB_2()
print(i1.m1())
print()
time.sleep(3)
print("End of an application")
print()

print("Example-4")
import time 
from abc import * 
class I_HUB_1(ABC):
    @abstractmethod 
    def m1(self):
        pass 
i1=I_HUB_1()
i1.m1()
print()
time.sleep(2)
print("End of an application")
