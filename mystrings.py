first_name = "      JOHn  "
last_name="Doe   "
email = "jOHN@mail.com"

first_name = first_name.title().strip()
last_name = last_name.strip()
email = email.lower()
full_name = first_name + " " + last_name
print(full_name, email)

#indexing - to get a single character from a string
print(email[-9])

#slicing-to get multiple characters from a string
#First part is index where you want to start
#second part is the index +1 where you want  to end
print(email[5:-4])
print(email.split("@"))#array
num = "7"
print(num.isnumeric())
print(len(full_name))