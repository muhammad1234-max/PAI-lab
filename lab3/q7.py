try:
    with open('replacement_needed.txt','w') as fileObj:
        fileObj.write("mally mellm meamhellm by the meamhore") #ive used a tongue twister but with the wrong alphabet
except:
    print("file could not be made")
    
def replace_Incorrect():
    try:
        with open('replacement_needed.txt','r') as fileObj:
            content = fileObj.read()
            print(f"the original content is {content}")
            
        wrong = 'm'
        right = 's'
        
        if wrong in content:
            content = content.replace(wrong,right) #replacing the wrong variable with the right one
            print(f"corrected content is : {content}")
        else:
            print("no corrections can be made")
    except:
        print("file could not be read")
        
replace_Incorrect() #function call
