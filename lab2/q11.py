#dictionary to store the marks of the students for 4 papers
students = {
    "Muhammad":[100,95,85,100],
    "Ali":[78,68,97,80],
    "Ahmed":[34,65,78,98],
    "Farukh":[100,97,68,79]
}

def add_grade(name,grade):
    if name in students:
        students[name].append(grade)
        print(f"the grade {grade} is added to {name}'s record")
    else:
        print(f"{name} is not in the system")
        
def calc_avg(name):
    if name in students:
        marks = students[name] #storing the list of marks in another list
        avg = sum(marks)/len(marks)
        print(f"{name}'s average is{avg}")
    else:
        print(f"{name} is not in the system")
        
def add_student(name):
    if name not in students:
        students[name] = [] #intializing a new key value pair in the dictionary with empty list of marks
        print(f"{name}'s record was added in the database")
    else:
        print(f"the students's record already exists in the database")
        
def remove(name):
    if name in students:
        del students[name] #removing a key-valu pair from the dictionary
        print(f"record of {name} removed from the system")
    else:
        print(f"{name} is not in the system")
        

add_grade("Muhammad",100)
calc_avg("Muhammad")
add_student("akbar")
remove("Ali")
