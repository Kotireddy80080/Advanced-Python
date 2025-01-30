import time
from abc import * 
class I_HUB_1:
    @abstractmethod 
    def m1(self):
        pass 
i1=I_HUB_1()
i1.m1()
print()
time.sleep(2)
print("end of the application")