#output 2
trainees=["John",[2,["James","Mary"]]]
print(trainees[1][0])

#output james
print(trainees[1][1][0])

#Append 56 at the end
trainees.append("56")
print(trainees)

#add mike between james and mary
trainees[1][1].insert(1,"mike")
print(trainees)

#change the value of 2 to 8
trainees[2] = 8
print(trainees)

#remove john and mary from the list

trainees.remove("John")
print(trainees)
# trainees[0][1].remove("Mary")

#using function determine the length of the list
print(len(trainees))