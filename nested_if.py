age=int(input("Enter your age:"))

if age<0:
    print("please enter a valid age")
else:
    if age<13:
        print("you are a child")
    elif age>=13 and age<18:
        print("you are a teenager")  
    else:
        print("you are an adult")  


       
