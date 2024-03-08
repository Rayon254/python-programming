# # Take three inputs from a user, separately. Print the largest of the numbers.
# #     Hint: Determine what type of data is taken in as input


num1=float(input("enter number:"))
num2=float(input("enter number:"))
num3=float(input("enter number:"))
if(num1>=num2 and num1>=num3 ):
    print(num1," is the largest")
elif(num2>=num1 and num2>=num3):
    print(num2," is the largest")
else:
    print(num3," is the largest")

# # Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”, otherwise display “Normal temperature”
# temp=float(input("enter temperature:"))
if(temp>30):
    value="The temperature is too high"
elif(temp>=15 and temp<=30):
    value="Normal temperature"
elif(temp>=0 and temp<15):
    value="Low temperature"
else:
    value="Extremely cold"

    print(value)


age=int(input("enter age:"))
if(age>=18):
    print("Eligible")
else:
    print("Not eligible")
