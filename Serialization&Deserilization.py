print("serilization")
import time 
import json 
D1={}
D1['Pid']=1001 
D1['Pname']="Mobile_1"
D1['Price']=29000 
D1['Company']="Samsung" 
D1['P_status_1']=True 
D1['P_Status_2']=None 
print()
print("====OS=====")
with open("ihub_111.txt","w") as f:
    json.dump(D1,f)
    print()
    print("OS is done successfully ...")
print()
time.sleep(3)
print("End of an application")


print("Deserilization")
import time 
import json 
D1={}
D1['Pid']=1001 
D1['Pname']="Mobile_1"
D1['Price']=29000 
D1['Company']="Samsung" 
D1['P_status_1']=True 
D1['P_Status_2']=None 
print()
print("====OD=====")
with open("ihub_111.txt","r") as f:
    obj1=json.load(f)
    print(obj1)
    print()
    for a1,a2 in obj1.items():
        print(a1,"---",a2)
print()
time.sleep(3)
print("End of an application")