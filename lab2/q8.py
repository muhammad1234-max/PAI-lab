#some conversion rates i took from the internet at that time so accuracy might not be exact
PKR_TO_USD = 0.0036
PKR_TO_INR = 0.30
PKR_TO_EUR = 0.0032
PKR_TO_YEN = 0.52

print("---currency exchange system---")
print("choose from following options:\n1)EUR\n2)USD\n3)PKR\n4)INR\n5)YEN\n")
choice1 = input("enter the currency you want to exchange: ")
amount = float(input("enter the amount you want to convert:"))
print("choose from following options:\n1)EURO\n2)DOLLAR\n3)PKR\n4)INR\n5)YEN\n")
choice2 = input("enter the currency you want to convert into: ")
choice1 = choice1.upper()
choice2 = choice2.upper()
#first we will convert whatever amount in whatever currency was given to pkr as a standard
#and then we will convert from pkr to the desired currency
converting_rate=0
if choice1 == "PKR":
    converting_rate = 1.0
elif choice1 == "DOLLAR":
    converting_rate = 1 / PKR_TO_USD
elif choice1 == "EUR":
    converting_rate = 1 / PKR_TO_EUR
elif choice1 == "INR":
    converting_rate = 1 / PKR_TO_INR
elif choice1 == "YEN":
    converting_rate = 1 / PKR_TO_YEN
else:
    print("invalid currency symbol for currency being converted entered")

#now we will convert whatever currency was entered to pkr as a standard
standard = amount * converting_rate

#now we will convert from pkr to the desired currency to convert to
if choice2 == "PKR":
    converting_rate = 1.0
elif choice2 == "DOLLAR":
    converting_rate =  PKR_TO_USD
elif choice2 == "EUR":
    converting_rate =  PKR_TO_EUR
elif choice2 == "INR":
    converting_rate =  PKR_TO_INR
elif choice2 == "YEN":
    converting_rate =  PKR_TO_YEN
else:
    print("invalid currency symbol to convert entered")

converted = standard * converting_rate
print(f"after converting {choice1} currency into {choice2} currency the amount is {converted}")
