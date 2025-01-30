import time 
from abc import * 
class I_HUB_IT_SERVICES(ABC):
    @abstractmethod 
    def m1(self):
        pass 
    @abstractmethod 
    def m2(self):
        pass 
class MYSQL_DB(I_HUB_IT_SERVICES):
    def m1(self):
        print("Connecting to MYSQL_DB for Indian_Userrs")
    def m2(self):
        print("Disconneting form MYSQL_DB for Indain_Users")
class MONGO_DB(I_HUB_IT_SERVICES):
    def m1(self):
        print("Connecting to MONGO_DB for USA_Userrs")
    def m2(self):
        print("Disconneting form MONGO_DB for USA_Users")
class Oracle(I_HUB_IT_SERVICES):
    def m1(self):
        print("Connecting to Oracle for Cananda_Userrs")
    def m2(self):
        print("Disconneting form Oracle for Canada_Users")
class PostGreSQL(I_HUB_IT_SERVICES):
    def m1(self):
        print("Connecting to PosGRESQL for chinese_Userrs")
    def m2(self):
        print("Disconneting form Oracle for Chinese_Users")
DB_Name=input("Enter the Database_Name:")
X1=globals()[DB_Name]
obj1=X1()
time.sleep(3)
obj1.m1()
print()
time.sleep(3)
obj1.m2()
print()
time.sleep(3)
print("End of an application")