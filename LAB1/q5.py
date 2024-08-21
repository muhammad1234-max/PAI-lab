test_list = []
ran = int(input("enter the size of the list: "))

for x in range(ran):
    print(f"enter the {x+1}th value: ")
    val = int(input())
    test_list.append(val)

limit = int(input("the limit below which you want the values to be deleted: "))

#List compression
test_list = [x for x in test_list if x >= limit]

print(test_list)
