



# Write a program that displays a numbers 1 to 50 inside a list
numbers= list(range(1,51))
print(numbers)


# From 1 above display the ones divisible by 7 or 5 inside a list.

divisible_by_7=[]

for i in numbers:
    if i%7==0:
        divisible_by_7.append(i)
print(divisible_by_7)

# Find sum and average of values in the range between 10 to 40.

num=list(range(10,41))
sum=0
average=[]

for i in num:
    sum+=i 
    average.append(i)  
    avg=sum/len(average)
print(sum)
print(avg)



# Put in a list the first 10 odd numbers between 10 to 50. 


odd=[]
for i in range(10,51):
    if i%2!=0:
     odd.append(i)
odd2=odd[0:10]
print(odd)


# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number=int(input("Enter number:"))
for i in range(1,11):
    num=(number*i)
    print(f"{number} * {i} = {num}")




# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop

even=0
for i in range(1,51):
    if i%2==0:
     even +=1
print(even)