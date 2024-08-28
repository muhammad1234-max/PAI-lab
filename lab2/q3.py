url = input("enter your url: ")

#lstrip will remove all the psecified characters from the left side
new_url = url.lstrip("https://.")
#concatenating the string
print(new_url+".com")
