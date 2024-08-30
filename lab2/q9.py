filename = "test.txt"
#try-except block used for exception catching
try:
    #creating the file and adding some random text to it
    with open(filename, 'w') as file:
        file.write("random text blah blah blah blah whatever")

    print(f"'{filename}' has been created")
#if by any chance file isnt made then a exception is raised
except Exception as e:
    print(f"An error occurred while makig the file: {e}")


try:
    #now we will open fle in read mode and count the characters
    with open(filename, 'r') as file:
        text = file.read()#using function to read the file

        #counting characters
        char_count = len(text)

        #counting words
        words = text.split() #splitting all the words in the text with the whitespace b/w wach words
        word_count = len(words)

        print(f"Total number of characters:{char_count}")
        print(f"Total number of words:{word_count}")

#again if some errror happens so exception is raised
except FileNotFoundError:#i have used a standard error for this situation
    print(f"'{filename}' was not found.")

