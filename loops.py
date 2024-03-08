# #write numbers between 0 and 1000 in a list

numbers=list(range(1,1001))
print(numbers)

# syntax for loop

for i in numbers:
    if i%2==0:
        print(i)

#display numbers between 1000 and 2000 divisible by 7

num=list(range(1000,2001))
divisible_by_7=[]

for i in num:
    if i%7==0:
        divisible_by_7.append(i)
print(divisible_by_7)


#save numbers that
#are only divisible by 5 and 7 and between 0 to 500 in a list


divisible=[]
for i in  range(0,501):
    if i%5==0 and i%7==0:
        divisible.append(i)
print(divisible)



fruits=["cherry","mango","apple","orange"]
for fruit in fruits:
    if fruit=="apple":
        print("available")
   

#write a program tha calculates the sum of all numbers
#from 1 to 100 using for loop

sum=0
for num in  range(1,101):
    sum+=num   
print(sum)
