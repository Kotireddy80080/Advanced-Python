print("assertion") #"debugging"
print("Example-1")
eid=1006
eid>1006                #"in the code line 3 is missing and executed then use assert keyword infront of 3 rd line"
print()
print("eid is:",eid)
print()


print("Developers code")
import time 
def Test_Add_Case1(X1,X2):
    return X1*X2 
if(__name__=="__main__"):
    print(Test_Add_Case1(2,5))
    print()
    print(Test_Add_Case1(10,15))
    print()
    print(Test_Add_Case1(120,150))
    print()
    print(Test_Add_Case1(190,120))
print()
time.sleep(2)
print("End of an application")

print("Testers code")
import time 
def Test_Add_Case1(X1,X2):
    return X1*X2 
assert Test_Add_Case1(2,5)==7,"2+5=7"
assert Test_Add_Case1(10,15)==25,"10+15=25"
assert Test_Add_Case1(120,150)==270,"120+150=270"
assert Test_Add_Case1(190,120)==310,"190+120=310"
if(__name__=="__main__"):
    print(Test_Add_Case1(2,5))
    print()
    print(Test_Add_Case1(10,15))
    print()
    print(Test_Add_Case1(120,150))
    print()
    print(Test_Add_Case1(190,120))
print()
time.sleep(2)
print("End of an application")


print("Developers code")
import time 
def Test_Add_Case1(X1,X2):
    return X1+X2 
assert Test_Add_Case1(2,5)==7,"2+5=7"
assert Test_Add_Case1(10,15)==25,"10+15=25"
assert Test_Add_Case1(120,150)==270,"120+150=270"
assert Test_Add_Case1(190,120)==310,"190+120=310"
if(__name__=="__main__"):
    print(Test_Add_Case1(2,5))
    print()
    print(Test_Add_Case1(10,15))
    print()
    print(Test_Add_Case1(120,150))
    print()
    print(Test_Add_Case1(190,120))
print()
time.sleep(2)
print("End of an application")
