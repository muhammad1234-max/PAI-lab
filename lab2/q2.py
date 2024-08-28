vowels = {'a','e','i','o','u','A','E','I','O','U'}

test_string = input("enter a string: ")

last_char = test_string[len(test_string)-1] #to access the last character of the entered string

if last_char in vowels:
    print(f"the last character {last_char} of the entered string {test_string} is a vowel")
else:
    print(f"the last character {last_char} of the entered string {test_string} is a consonant")
