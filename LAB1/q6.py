maths = int(input("enter the maths marks: "))
physics = int(input("enter the physics marks: "))
chemistry = int(input("enter the chemistry marks: "))

marks_dict ={
    "maths":0,
    "physics":0,
    "chemistry":0
}

marks_dict["maths"] = maths
marks_dict["chemistry"] = chemistry
marks_dict["physics"] = physics

sum = sum(marks_dict.values())
avg = sum/len(marks_dict)

print(f"the average of all the marks is{avg}")

highest_subject = max(marks_dict, key=marks_dict.get)
highest_marks = marks_dict[highest_subject]

print(f"Subject with Highest Marks: {highest_subject} and the marks are ({highest_marks})")
