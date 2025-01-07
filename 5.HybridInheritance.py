print("Inheritance")
print("5.Hybrid  Inheritance")
print("MRO")  #"know mro of each class"
import time 
class A_class:pass 
class B_class(A_class):pass 
class C_class(A_class):pass 
class D_class(B_class,C_class):pass 
print()
print("====MRO OF A_CLASS====")
print(A_class.mro())
print()
print("====MRO OF B_CLASS====")
print(B_class.mro())
print()
print("====MRO OF C_CLASS=====")
print(C_class.mro())
print()
print("====MRO OF D_CLASS====")
print(D_class.mro())
print()
time.sleep(2)
print('End of an application')

print("example-2")
import time 
class A_class:pass 
class B_class:pass 
class C_class:pass 
class X_class(A_class,B_class):pass 
class Y_class(B_class,C_class):pass 
class Z_class(X_class,Y_class,C_class):pass 
print()
print(A_class.mro())
print()
print(B_class.mro())
print()
print(C_class.mro()) 
print()
print(X_class.mro())
print()
print(Y_class.mro())
print()
print(Z_class.mro())
print()
time.sleep(2)
print("End of an application")