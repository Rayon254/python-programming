#Convert a float to an integer with an inbuilt function in Python
temp = 56.8926 
temp = int(round(temp,0))
print(temp)


# Convert the float below to give the results as follows
temp = 56.8926 
temp = round(temp,2)
print(temp)

# Convert the float below to give the results as follows
temp = 56.8926
temp = round(temp,3)
print(temp)

# Convert the float below to give the results as follows
temp=56.8926 
temp=str(temp)
temp=temp[3:7]
temp=float(temp[0]+"."+temp[1:4])
print(temp)

# NB: Use string  slice & concatenation, but have result as float 



#to 8.926 
