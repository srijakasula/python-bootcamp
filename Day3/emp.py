class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def empdisplay(self):
        print(self.name,self.role)
class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):
        print('hiring for the manager role')
cobj=Company('wipro','gachibowli')
eobj=Employee('srija','dev',90000)
eobj.empdisplay()
print(cobj._hiring())