for x in range(0,51):
    if(x==0):
        print("fizzbuzz")
    elif(x % 3 == 0):
        print("fizz")
    elif(x % 5 == 0):
        print("buzz")
    elif(x % 3 ==0 and x % 5 == 0):
        print("fizzbuzz")
    else:
        print(x)
