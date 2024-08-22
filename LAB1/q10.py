num_list = []
length = int(input("enter the length of the list you want to input: "))

for x in range(length):
    num = int(input(f"enter the {x+1}th value: "))
    num_list.append(num)

biggest = num_list[0]

#loop starts checking from the second element
for x in range(1, len(num_list)):  
    if num_list[x] > biggest:
        biggest = num_list[x]

print(f"the biggest number in the list is {biggest}")
