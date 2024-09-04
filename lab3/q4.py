name = input("enter the name: ")
cnic = int(input("enter the CNIC number: "))
age = int(input("enter the age: "))
salary = int(input("enter the salary earned: "))
try:
    with open("text4.txt","w") as fileObj:
        fileObj.write(f"name:{name}, CNIC:{cnic}, age:{age}, salary: {salary} ")
        print("initial data entered successfully")
except FileNotFoundError:
    print("the file could not be formed")

contact = int(input("enter the contact number: "))
try:
    with open("text4.txt",'a') as fileObj:
        fileObj.write(f"contact{contact}")
        print("extra info added")
except FileNotFoundError:
    print("file not found")
