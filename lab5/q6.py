from abc import ABC,abstractmethod #importing abstract classes

class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    @abstractmethod
    def calc_Bonus(self):
        pass
    
class Manager(Employee):
    
    def calc_Bonus(self):
        return self.salary * 0.2
    
    def hire(self):
        return "the manager is hiring someone"
    
class Developer(Employee):
    
    def calc_Bonus(self):
        return self.salary * 0.1
    
    def writeCode(self):
        return "developer is writing code"
    
    
class SeniorManager(Manager):
    
    def calc_Bonus(self):
        return self.salary * 0.3
    
employee1 = Manager('Ahmed',100000)
employee2 = Developer("Syra",80000)
employee3 = SeniorManager("Muhammad",1000000)

print(employee1.calc_Bonus())
print(employee2.calc_Bonus())
print(employee3.calc_Bonus())
print(employee1.hire())
print(employee2.writeCode())
