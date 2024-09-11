a = ["He", "th", "i", "sal"]
b = ["llo", "is", "s", "man"]
c = [a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3]]

print(list(c))

print("output after attempting the above code in a single line query.")
print([x + y for x, y in zip(["He", "th", "i", "sal"], ["llo", "is", "s", "man"])])



