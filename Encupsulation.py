class Employees_Class:
    def setEid(self,Eid):
        self.Eid=Eid
    def getEid(self):
        return self.Eid 
    def setEname(self,Ename):
        self.Ename=Ename 
    def getEname(self):
        return self.Ename
    def setEsal(self,Esal):
        self.Esal=Esal 
    def getEsal(self):
        return self.Esal
    def setDesign(self,Design):
        self.Design=Design 
    def getDesign(self):
        return self.Design 
    def setCompany(self,Company):
        self.Company=Company 
    def getCompany(self):
        return self.Company
e1=Employees_Class()
e1.setEid(1001)
e1.setEname("Jessica_1")
e1.setEsal(29000)
e1.setDesign("DAD developer")
e1.setCompany("HCL")
print()
print("=====Employees_Details====")
print("Eid is:",e1.getEid())
print("Ename is:",e1.getEname())
print("Esal is:",e1.getEsal())
print("Design is:",e1.getDesign())
print("Company is:",e1.getCompany())
print()