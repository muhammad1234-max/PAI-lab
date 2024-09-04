import json

def save_to_json(file_path, data):
    
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
        print(f"Data successfully saved to {file_path}.")
    except:
        print("couldnt add data to the file")

def load_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except:
        print("data could not be read")

def max_Age(data):
    #checks if dictionary is empty
    if not data:
        print("No data to process.")
        return
    
    try:
        max_age = max(data.values())
        persons_with_max_age = [name for name, age in data.items() if age == max_age] #ternary operator used
        print(f"Person(s) with maximum age ({max_age}): {', '.join(persons_with_max_age)}") #formatted string
        age_counts = {}
        for age in data.values():
            if age in age_counts:
                age_counts[age] += 1
            else:
                age_counts[age] = 1
        duplicate_ages = [age for age, count in age_counts.items() if count > 1]  #ternary operator
        
        if duplicate_ages:
            print(f"There are other people with the following ages also duplicated: {', '.join(map(str, duplicate_ages))}")
        else:
            print("No other ages are duplicated.")
    
    except :
        print("couldnt read the data")

#dictionary from the question
dictionary = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}
file_path = 'text5.json'
save_to_json(file_path, dictionary)
loaded_data = load_from_json(file_path)
max_Age(loaded_data)
