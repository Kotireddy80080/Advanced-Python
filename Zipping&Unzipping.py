print("zipping")
import time 
from zipfile import * 
f1=ZipFile("ihub_3.zip","r",ZIP_STORED)
X1=f1.namelist()
print(X1)
print()
f1.close()
print()
print("End of an application")


print("Unzipping")
import time 
from zipfile import * 
f1=ZipFile("ihub_3.zip","r",ZIP_STORED)
X1=f1.namelist()
print(X1)
print()
f1.close()
print()
print("End of an application")