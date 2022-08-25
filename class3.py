class Parent_class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name:",self.name)
        print("age:",self.age)
class Child_class(Parent_class):
    def __int__(self,name,age,city):
        super().__init__(name,age)
        self.city=city
    def show(self):
        super().show()
        print("city:",self.city)
class Grandchild_class(Child_class):
    def __int__(self,name,age,city,country):
        super().__init__(name,age,city)
        self.country=country
    def show(self):
        super().show()
        print("country:",self.country)
p=Parent_class("John",30)
p.show()
c=Child_class("John",30,"kerala")
c.show()
g=Grandchild_class("John",30,"Kerala","India")
g.show()

