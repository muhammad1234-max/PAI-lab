def employee(name,salary=10000):
    after_tax = salary - (salary*0.02)
    print("employee name: ",name)
    print("employee salary after tax: ",after_tax)

name = input("enter the employee name: ")
salary = int(input("enter the salary before tax:"))
employee(name,salary)
