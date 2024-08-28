size = int(input("Enter the length of the list: "))
test_list = [0] * size  #initialize a list of the given size with zeroes

for x in range(size):
    test_list[x] = int(input(f"Enter value {x + 1}: "))  

mul = 1
for x in range(size):
    mul = mul * test_list[x]  

print("The product of all elements in the list is:", mul)
