try:
    # Opening file in read and write mode
    with open('test2.txt', 'w') as fileObj:
        fileObj.write("some random text very gibberish random and stupidly random text")  # Writing text to the file
        
except FileNotFoundError:
    print( "The file was not found.")


try:
    with open('test2.txt','r+') as fileObj:
        content = fileObj.read()
        changed = content.replace("random","smart")
        fileObj.seek(0) #moving the file pointer back to start

        fileObj.write(changed) #writing back the modified content back to the file
        fileObj.truncate() #adjusting file sixe based on new content
        print("content changed successfuly")

except FileNotFoundError:
    print("file coould not be found or created")
