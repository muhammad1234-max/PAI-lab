# split is storing all values seperately and splitting based on spaces
list1 = input("Enter the first list of elements, separat it by spaces: ").split()
list2 = input("Enter the second list of elements, separat it by spaces: ").split()


if len(list1) != len(list2):
    print("wrong both lists must have same number of elements")
else:
    test_dict = {}
    for i in range(len(list1)):
        test_dict[list1[i]] = list2[i]

    print("dictionary from combined lists:", test_dict)