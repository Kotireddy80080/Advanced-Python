print("Example-1")
import time 
def Test_Case1(name):
    print("Name of the language is:",name)
if(__name__=="__main__"):
    Test_Case1("Python")
print()
time.sleep(2)
print("End of an application")

print("Example-2")
import time
def Test_Case2(func):
    def inner(name):
        if(name=="Python"):
            print(name,":Meant for general purpose application")
        else:
            func(name)
    return inner
@Test_Case2
def Test_Case1(name):
    print("Name of the language is:",name)
if(__name__=="__main__"):
    Test_Case1("Python")
print()
time.sleep(2)
print("End of an application")