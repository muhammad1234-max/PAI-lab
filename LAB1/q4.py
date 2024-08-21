test_list = []
sum = 0
ran = int(input("enter the size of the list: "))

for x in range(ran):
    print(f"enter the {x+1}th value: ")
    val = int(input())
    test_list.append(val)

for x in range(len(test_list)):
    sum = sum + test_list[x]

print(f"the sum of all the values in the list is {sum}")
