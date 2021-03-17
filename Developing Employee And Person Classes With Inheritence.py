#  Developing Employee And Person Classes With Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print ( 'Eat Biryani And Drink Beer' )
class Employee(Person):
    def __init__(self, name, age, eno, esal):
        self.name = name
        self.age = age
        self.eno = eno
        self.esal = esal
    def work(self):
        print('Coding Python Programs')
    def empInfo(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)
e = Employee('Arjun', 39, 10001, 10000)
e.eatndrink()
e.work()
e.empInfo()
