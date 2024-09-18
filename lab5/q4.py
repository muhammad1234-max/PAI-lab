class Student:
    def __init__(self, id , name):
        self.id = id
        self.name  = name

    def print(self):
        print(f"student name: {self.name}\nstudent ID: {self.id}")

class Marks(Student):
    def __init__(self, id, name, ds,algo,cal):
        super().__init__(id,name)
        self.ds = ds
        self.algo = algo
        self.cal = cal

    def print(self):
        super().print()
        print(f"DS:{self.ds}\nALGO:{self.algo}\nCAL:{self.cal}")

class Result(Marks):
    def __init__(self,id,name,ds,algo,cal):
        super().__init__(id,name,ds,algo,cal)

    def calc(self):
        print(f"the total of all the marks is: {self.ds+self.algo+self.cal}\nthe average is: {(self.ds+self.algo+self.cal)/3}")

final = Result(230068,"Muhammad",100,90,80)
final.print()
final.calc()        
