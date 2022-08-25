class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def increase_salary(self):
        self.salary=self.salary+1000
    def decrease_salary(self):
        self.salary=self.salary-200
    def display(self):
        print(self.name,self.age,self.salary)
obj=Employee("ASWATHI",21,25000)
obj.display()
obj.increase_salary()
obj.display()
obj.decrease_salary()
obj.display()
print(obj.name)
print(obj.age)
print(obj.salary)
print("*************************")
obj2=Employee("ANUSREE",21,3000)
obj2.display()
obj2.increase_salary()
obj2.display()
obj2.decrease_salary()
obj2.display()