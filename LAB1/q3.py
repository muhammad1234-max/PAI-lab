ran = int(input("enter the number of values you want to enter in your list: "))
test_list = []
count =0

for x in range(ran):
    print(f"enter the {x+1} value:")
    value = int(input())
    test_list.append(value)


for x in range(len(test_list)):
    if test_list[x] % 2 == 0:
        count = count + 1

print(f"the even numbers in the list are {count}")
