def write_ques_to_file():
    try:
        sentence = input("enter a question:")
        if sentence.strip().endswith('?'): #checks if it is a question
            with open('questions.txt', 'a') as fileObj:
                fileObj.write(sentence + "\n") #appends question to the file
            print("question added to the file")
        else:
            print("That is not a question so wont be added to the file")
    except:
        print("Error: unable to open file")
        
write_ques_to_file()
