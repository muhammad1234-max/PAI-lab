def build_message(**info):
    #an empty list to hold the pieces of the message
    message_parts = []

    # Iterate over the keyword arguments like a dictionary key-value pair
    for key, value in info.items():
        #capitalize(change first letter to capital) the key and format the txt
        message_parts.append(f"{key.capitalize()}: {value}")
    
    #comine all parts into a single string with commas 
    message = ", ".join(message_parts)
    
    return message

message = build_message(name="muhammad", age=20, city="karachi", occupation="student")
print(message)

