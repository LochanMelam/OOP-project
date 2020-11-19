u=int(input("Please enter the username given by the company:"))
class Employee:
    def __init__(self,n,a,g,p,s,b,u):
        self.name=n
        self.age=a
        self.sex=g
        self.position=p
        self.salary=s
        self.password=b
        self.user=u
    def display(self):
        print("Employee:",self.name)
        print("Age:",self.age)
        print("Gender:",self.sex)
        print("Designation:",self.position)
        print("salary:",self.salary)
        print("Password:",self.password)
        print("Username given:",self.user)
e1=Employee("Rita",34,"Female","Manager","2L","pouthg",300987)
e1.display()
