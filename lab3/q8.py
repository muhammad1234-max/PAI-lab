try:
    num1 = int(input("enter number 1: "))
    num2 = int(input("enter number 2: "))

    answer = num1/num2
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("please only enter integers for input")
else:
    print(f"the result of the calculation is {answer}")


    
