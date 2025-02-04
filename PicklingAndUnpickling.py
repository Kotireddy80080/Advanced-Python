print("Pickling(Packing) & Unpickling(Unpacking)")

print("pickling(packing")
import time 
import pickle 
class Train_Information_Class:
    def __init__(self,tno,tname,arrtime,depttime,date,source,destination):
        self.tno=tno 
        self.tname=tname 
        self.arrtime=arrtime 
        self.depttime=depttime 
        self.date=date 
        self.source=source 
        self.destination=destination
    def m1(self):
        print("====Train_Information====")
        print("tno is:",self.tno)
        print("tname is:",self.tname)
        print("Arrtime is:",self.arrtime)
        print("Depttime is:",self.depttime)
        print("Date is:",self.date)
        print("Source is:",self.source)
        print("Destination is:",self.destination)
with open("ihub_5.txt","wb") as f:
    t1=Train_Information_Class(1001,"RE","11:00 AM","12:30 PM","19/11/2024","Hyderabad","Delhi")
    pickle.dump(t1,f)
    print()
    print("Pickling/Packing is done successfully ...")
print()
time.sleep(2)
print("End of an application")



print("unpickling(unpacking)")
import time 
import pickle 
class Train_Information_Class:
    def __init__(self,tno,tname,arrtime,depttime,date,source,destination):
        self.tno=tno 
        self.tname=tname 
        self.arrtime=arrtime 
        self.depttime=depttime 
        self.date=date 
        self.source=source 
        self.destination=destination
    def m1(self):
        print("====Train_Information====")
        print("tno is:",self.tno)
        print("tname is:",self.tname)
        print("Arrtime is:",self.arrtime)
        print("Depttime is:",self.depttime)
        print("Date is:",self.date)
        print("Source is:",self.source)
        print("Destination is:",self.destination)
with open("ihub_5.txt","rb") as f:
    obj1=pickle.load(f)
    obj1.m1()
    print()
    print("Unpickling is done successfully ...")
   
print()
time.sleep(2)
print("End of an application")