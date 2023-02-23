#oops init method (simple,hirarchi)

class Emp:
    def __init__(self,mid,mname,msal):
        self.eId = mid
        self.eName = mname
        self.eSal = msal

    def display(self):
        print(self.eId,self.eName,self.eSal)


class SalesPerson(Emp):   #SalesPerson inheriting proprties of Emp Class
    def __init__(self,mid,mname,msal,msales,mcomm):
        Emp.__init__(self,mid,mname,msal)    #Emp class called here(inherit)
        self.eSales = msales
        self.eComm = mcomm

    def display(self):
        Emp.display(self)     #upper Emp display called here
        print(self.eSales,self.eComm)

class Manager(Emp):
    def __init__(self,mid,mname,msal,mfood,mfuel):
        Emp.__init__(self,mid,mname,msal)
        self.eFood = mfood
        self.eFuel = mfuel

    def display(self):
        Emp.display(self)
        print(self.eFood,self.eFuel)

class SalesManager(SalesPerson,Manager):
    def __init__(self,mid,mname,msal,msales,mcomm,mfood,mfuel):
        SalesPerson.__init__(self,mid,mname,msal,msales,mcomm)
        Manager.__init__(self,mid,mname,msal,mfood,mfuel)

    def display(self):
        SalesPerson.display(self)
        Manager.display(self)
        

#__main__

sp = SalesPerson(11111,'Tushar',21000,1000,21000)
sp.display()

m = Manager(10001,'suresh',30000,5000,6000)
m.display()


sm=SalesManager(101,'swapnil',35000,5000,10000,5000,3000)
sm.display()
