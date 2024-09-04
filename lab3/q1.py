try:
    # Opening file in read and write mode
    with open('test.txt', 'w') as fileObj:
        fileObj.write("some random text")  # Writing text to the file
        
except FileNotFoundError:
    print( "The file was not found.")

try:
    with open("test.txt",'r')as fileObj:
        content = fileObj.read()  # Reading the text from the file
        char_Count = len(content)  # Calculating the number of characters
        word_Count = len(content.split())  # Splitting the content on whitespaces and counting the number of words
        
        print(f"The number of characters is {char_Count} and the number of words are {word_Count}")

except FileNotFoundError:
    print("file not found")
        
