
# 1.Write a program that takes a student's 
# score input checks if the scores are between 0 and 100 and
#  prints their grade (A, B, C, D, or F) based on the following conditions:
# A: 90 and above
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: below 60
# otherwise prints invalid score

student_score=float(input("Enter Scores:"))

if(student_score>=0 and student_score<=100):
    if(student_score>=90):
        grade="A"
    elif(student_score>=80 and student_score<=89):
        grade="B"
    elif(student_score>=70 and student_score<=79):
        grade="C"
    elif(student_score>=60 and student_score<=69):
        grade="D"
    else:
        grade="F"
else:
        grade="invalid scores"

print(grade)



# 2.Write a program that asks the user to input two numbers
# checks if  both numbers are  are positive and then checks 
# if the sum of the numbers is even or odd.otherwise  print "negative numbers."


#f is used to put a variable inside a string i.e f"(sum) is even" f(formatted)
num1=float(input("Enter number:"))
num2=float(input("Enter number:"))


if(num1>0 and num2>0):
    print("positive")
    sum=num1+num2
    if(sum % 2==0):
        print(f"(sum) is even")
    else:
        print(f"(sum) is even")
else:
        print("negative numbers")

# 3.write a program that takes the user's input for a time in 24-hour format and converts
#  it to 12-hour format. Consider handling cases for noon and midnight appropriately.



time=input("Enter time:")

if len(time)==3:
    print(time.split(":")(1))
else:
    print("Invalid time")





