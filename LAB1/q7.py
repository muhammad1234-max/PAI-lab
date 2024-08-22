value = input("enter the string you want to reverse: ")

for x in range(len(value)):
    # index value of the last character is calculated in the first iteration and so on to reverse the string
    # the end='' makes sure all the printed reveresed characters are on the same line
    print(value[len(value)-x-1], end='')
