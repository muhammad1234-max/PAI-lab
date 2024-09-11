class student :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_biodata(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")


freshie = student("Muhammad",21)
freshie.print_biodata()
    
