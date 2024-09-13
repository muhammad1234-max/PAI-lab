class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def display_info(self):
        print(f"Name: {self.name}\nID:{self.id}")
        
class Marks(Student):
    
    def __init__(self, name, id, marks_algo,marks_DS, marks_calculus):
        super().__init__(name, id) #calling base class constructor
        self.marks_algo = marks_algo
        self.marks_DS = marks_DS
        self.marks_calculus = marks_calculus
        
    def display_info(self):
        super().display_info()
        print(f"Marks in Algorithms: {self.marks_algo}")
        print(f"Marks in Data Science: {self.marks_DS}")
        print(f"Marks in Calculus: {self.marks_calculus}")
        
class Result(Marks):
    
    def __init__(self, name, id, marks_algo,marks_DS, marks_calculus):
        super().__init__(name, id, marks_algo,marks_DS, marks_calculus)
        self.total_marks = 0
        self.avg = 0
    
    def calc(self):
        total_marks = self.marks_algo + self.marks_calculus + self.marks_DS
        avg = total_marks / 3
        return total_marks, avg
    
    def display_info(self):
        super().display_info()
        total, average = self.calc()
        print(f"the total marks: {total}\nThe average: {average}")
        
Student = Result("Muhammad",10068,90,90,90)
Student.display_info()    
