
#lists
days_of_the_week=["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday"]
print(days_of_the_week[2])

numbers=[1,2,3,4,[10,20,30],5,6,7,8]
print(numbers[4][1])

days_of_the_week=["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday"]
days_of_the_week[1] = "Friday"
print(days_of_the_week)

#list methods
#append is used to add an element into a list 
days_of_the_week.append("monday")

#deletes all elements in a list
days_of_the_week.clear

#copies a least to a new list
days_of_the_week.copy

#counts the appearance of an element in a list
days_of_the_week.count

#extends with another list
list=[1,2,3,4,5,6,7]
days_of_the_week.extend(list)
print(days_of_the_week)

#removes a specified alement
days_of_the_week.remove("Wednesday")

#pop() removes at the end
#insert() inserts into a specific index
days_of_the_week.insert(2,"friday")
#reverse() reverses elements in a list
#sort displays elements in order
#del days of the week
