subject1 = int(input("enter the marks of the first  out of 100: "))
subject2 = int(input("enter the marks of the second subjet out of 100: "))
subject3 = int(input("enter the marks of the third subject out of 100: "))

sub_dict = {"subject1":subject1,
            "subject2":subject2,
            "subject3":subject3}

sum = sum(sub_dict.values())
avg = sum/len(sub_dict)
percentage = (sum/300)*100
print(f"the average of the student is {avg} and the achieved percentage is {percentage}")
