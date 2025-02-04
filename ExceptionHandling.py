print("with try and except")
print("Example-1")
import time 
try:
    X1=int(input('Enter the value of X1:'))
    X2=int(input('Enter the value of X2:'))
    res1=X1//X2  
    print("The result_set is:",res1)
except BaseException as e:
    print('Exception_Name is:',e)
print()
time.sleep(2)
print('End of an application')

print("Example-2")
import time 
try:
    X1=int(input('Enter the value of X1:'))
    X2=int(input('Enter the value of X2:'))
    res1=X1//X2  
    print("The result_set is:",res1)
except Exception as e:
    print('Exception_Name is:',e)
print()
time.sleep(2)
print('End of an application')

print("Example-3")
import time 
try:
    X1=int(input('Enter the value of X1:'))
    X2=int(input('Enter the value of X2:'))
    res1=X1//X2  
    print("The result_set is:",res1)
except ArithmeticError as e:
    print('Exception_Name is:',e)
print()
time.sleep(2)
print('End of an application')

print("Example-4")
import time 
try:
    X1=int(input('Enter the value of X1:'))
    X2=int(input('Enter the value of X2:'))
    res1=X1//X2  
    print("The result_set is:",res1)
except ZeroDivisionError as e:
    print(X2,":Dear Customer a number is not divided by 0.Use anoher number")
print()
time.sleep(2)
print('End of an application')

print("more than one except and with one try block")
print("Example-1")
import time 
try:
    X1=int(input('Enter the value of X1:'))
    X2=int(input('Enter the value of X2:'))
    res1=X1//X2  
    print("The result_set is:",res1)
except ArithmeticError:
    print("ZE_Error")
except ZeroDivisionError:
    print("AE_Error")
except ValueError:
    print("Value_Error")
print()
time.sleep(2)
print("End of an application")


print("Example-2")
import time 
try:
    X1=int(input('Enter the value of X1:'))
    X2=int(input('Enter the value of X2:'))
    res1=X1//X2  
    print("The result_set is:",res1)
except ZeroDivisionError:
    print("ZE_Error")
except ArithmeticError:
    print("AE_Error")
except ValueError:
    print("Value_Error")
print()
time.sleep(2)
print("End of an application")

print("Default Except")
print("Example-1")
import time 
try:
    X1=int(input('Enter the value of X1:'))
    X2=int(input('Enter the value of X2:'))
    res1=X1//X2  
    print("The result_set is:",res1)
except ZeroDivisionError:
    print("ZE_Error")
except ArithmeticError:
    print("AE_Error")
except :
    print("Value_Error")
print()
time.sleep(2)
print("End of an application")


print("one Exception classes inside with except block")
import time 
try:
    X1=int(input("Enter the value of X1:"))
    X2=int(input("Enter the value of X2:"))
    res1=X1//X2 
    print("The result_set is:",res1)
except(ZeroDivisionError,ArithmeticError,ValueError) as e:
    print("Exception_Name is:",e)
print()
time.sleep(2)
print("End of an application")


print("finally block") # os._exit(0)- "status code can be 0,+ve,-ve numbers"
print("Example-1")
import time 
try:
    print("Python Developer")
    print()
except:
    print("Angular Developer")
    print()
finally:
    print("Full Stack Python Developer")
    print()
print()
time.sleep(2)
print("End of an application")


print("Example-2")
import time 
try:
    print("Python Developer")
    print()
    print(1000//0)
    
except:
    print("Angular Developer")
    print()
finally:
    print("Full Stack Python Developer")
    print()
print()
time.sleep(2)
print("End of an application")


print("Example-3")
import time 
import os
try:
    print("Python Developer")
    print()
    print(1000//0)
    os._exit(0) 
except:
    print("Angular Developer")
    print()
finally:
    print("Full Stack Python Developer")
    print()
print()
time.sleep(2)
print("End of an application")

print("Example-4")
import time 
import os
try:
    print("Python Developer")
    print()
    os._exit(0) 
    print(1000//0) 
except:
    print("Angular Developer")
    print()
finally:
    print("Full Stack Python Developer")
    print()
print()
time.sleep(2)
print("End of an application")

print("Example-5")
import time 
import os
try:
    print("Python Developer")
    print()
    os._exit(True) 
    print(1000//0) 
except:
    print("Angular Developer")
    print()
finally:
    print("Full Stack Python Developer")
    print()
print()
time.sleep(2)
print("End of an application")


print("Example-6")
import time 
import os
try:
    print("Python Developer")
    print()
    os._exit(False) 
    print(1000//0) 
except:
    print("Angular Developer")
    print()
finally:
    print("Full Stack Python Developer")
    print()
print()
time.sleep(2)
print("End of an application")


print("Example-7")
import time 
import os
try:
    print("Python Developer")
    print()
    os._exit(chr(65)) 
    print(1000//0) 
except:
    print("Angular Developer")
    print()
finally:
    print("Full Stack Python Developer")
    print()
print()
time.sleep(2)
print("End of an application")


print("Example-8")
import time 
import os
try:
    print("Python Developer")
    print()
    os._exit(ord('a')) 
    print(1000//0) 
except:
    print("Angular Developer")
    print()
finally:
    print("Full Stack Python Developer")
    print()
print()
time.sleep(2)
print("End of an application")


print("Example-9")
import time 
import os
try:
    print("Python Developer")
    print()
    print(1000//0) 
except:
    print("Angular Developer")
    print()
    os._exit(chr(65))
finally:
    print("Full Stack Python Developer")
    print()
print()
time.sleep(2)
print("End of an application")

print("working with except with esle block")
print("Example-1")
import time 
try:
    print("JavaScript Developer")
except:
    print("Angular Developer")
else:
    print("TypeScript Developer")
finally:
    print("Full Stack Python Developer")
print()
time.sleep(2)
print("End of an applicaiton")

print("Example-2")
import time 
try:
    print("JavaScript Developer")
    print(1000//0)
except:
    print("Angular Developer")
else:
    print("TypeScript Developer")
finally:
    print("Full Stack Python Developer")
print()
time.sleep(2)
print("End of an applicaiton")


print("An exception can be occur in 3 blocks")
print("Example-1")
import time 
try:
    print("Outer_Try_Block")
    try:
        print("Inner_Try_Block")
    except:
        print("Inner_Except_Block")
    else: 
        print("Inner_Else_Block")
    finally:
        print("Inner_Finally_Block")
except:
    print("Outer_Except_Block")
else:
    print("Outer_Else_Block")
finally:
    print("Outer_Finally_Block")
print()
time.sleep(2)
print("End of an application")

print("Example-2")
import time 
try:
    print("Outer_Try_Block")
    print(1000//0)
    try:
        print("Inner_Try_Block")
    except:
        print("Inner_Except_Block")
    else: 
        print("Inner_Else_Block")
    finally:
        print("Inner_Finally_Block")
except:
    print("Outer_Except_Block")
else:
    print("Outer_Else_Block")
finally:
    print("Outer_Finally_Block")
print()
time.sleep(2)
print("End of an application")


print("Example-3")
import time
try:
    print("Outer_Try_Block")
    try:
        print("Inner_Try_Block")
        print(1000//0)
    except:
        print("Inner_Except_Block")
    else: 
        print("Inner_Else_Block")
    finally:
        print("Inner_Finally_Block")
except:
    print("Outer_Except_Block")
else:
    print("Outer_Else_Block")
finally:
    print("Outer_Finally_Block")
print()
time.sleep(2)
print("End of an application")


