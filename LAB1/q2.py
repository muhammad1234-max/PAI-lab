num1= int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operation = str(input("enter the operation you want to conduct(+,-,/,*): "))


if operation == '+':
    print( -num1 - num2)
elif operation == '-':
    print( num1 - num2)
elif operation == '/':
    if num2==0:
        raise("zero division error")
    else:
        print( num1/num2)
else:
    print( num1*num2)
    
