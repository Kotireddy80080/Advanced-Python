print("Example-1")  # using yield keyword and next
import time 
def Test_Case1():
    str1="Core Python"
    yield str1 
    str2="Advance Python"
    yield str2 
    str3="FrontEnd with Django"
    yield str3 
    str4="Angular/React with Flask"
    yield str4

if(__name__=="__main__"):
    x1=Test_Case1()
    print(next(x1))
    print()
    print(next(x1))
    print()
    print(next(x1))
    print()
    print(next(x1))
print()
time.sleep(2)
print("End of an application")

print("Example-2")
import time 
def Test_Case1():
    str1="Core Python"
    yield str1 
    str2="Advance Python"
    yield str2 
    str3="FrontEnd with Django"
    yield str3 
    str4="Angular/React with Flask"
    yield str4

if(__name__=="__main__"):
    x1=Test_Case1()
    for x2 in x1:
        print(x2)
 
print()
time.sleep(2)
print("End of an application")


print("Example-3")
import time 
def Test_Case1():
    T1=(x*x for x in range(15))
    print(T1)
    print()
    print(type(T1))
if(__name__=="__main__"):
    Test_Case1()
print()
time.sleep(2)
print("End of an application")

print("Example-4")
import time 
def Test_Case1():
    L1=[x*x for x in range(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)]
    print(L1)
   
if(__name__=="__main__"):
    Test_Case1()
print()
time.sleep(2)
print("End of an application")

print("Example-5")
import time 
def Test_Case1():
    str1="Core Python"
    yield str1 
    str2="Advance Python"
    yield str2 
    str3="FrontEnd with Django"
    yield str3 
    str4="Angular/React with Flask"
    yield str4

if(__name__=="__main__"):
    x1=Test_Case1()
    print(next(x1))
    print()
    print(next(x1))
    print()
    print(next(x1))
    print()
    print(next(x1))
    print()
    print(next(x1))
print()
time.sleep(2)
print("End of an application")