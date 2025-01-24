print("Method overriding and Construcrtor overriding")
class Product_1:
    def __init__(self,Pid,Pname):
        self.Pid=Pid 
        self.Pname=Pname 
    def m1(self):
        print("Pid is:",self.Pid)
        print("Pname is:",self.Pname)
class Product_2(Product_1):
    def __init__(self,Pid,Pname,Price,Company,M_date,Exp_date):
        super().__init__(Pid,Pname)
        self.Price=Price 
        self.Company=Company 
        self.M_date=M_date 
        self.Exp_date=Exp_date 
    def m2(self):
        super().m1() 
        print("Price is:",self.Price)
        print("Compnay is:",self.Company)
        print("M_date is:",self.M_date)
        print("Exp_date is:",self.Exp_date)
p1=Product_2(1001,"Mobile_1",27000.0,"Samsung","12/12/2024","12/12/2025")
p1.m2()
print()