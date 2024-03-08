
#Find wednesday using an index

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
print(days[2])

#length
print(len(days))

#replace thursday with thur
my_list=list(days)
my_list[3]= "thur"
days=tuple(my_list)
print(days)

my_list=list(days)
my_list[6]="sun"
days=tuple(my_list)
print(days)