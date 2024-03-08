name = "  JOHn  ."
print(name.lower().strip().replace(".",""))


sentence_one = ("The Dog Breed is German Shepherd")
print(sentence_one[8:23])


sentence_two = ("Defeats for the Clinton forces, this was her moment of triump")
print(sentence_two[16:30])

sentence_three = ("The lazy dog; ran so fast; it hit the wall.")
print(len(sentence_three.split(";")))


first_name="  Joh.n"
last_name="   Do,e"
full_name = first_name.strip().replace(".","")+" "+last_name.strip().replace(",","")
print(full_name)

r = '["E","W","C"]'
print("".join(filter(str.isalpha,r)))



