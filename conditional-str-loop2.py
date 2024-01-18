i=0
for a_num in range(-5,5):
    i=a_num
#print(i)

mystery_int=5
facto =mystery_int
for i in range(1, mystery_int):
    facto = facto * (mystery_int - i)
print(facto)

a_string = "Indices! Yay!"
a_character = a_string[3]
print("The character is", a_character)

some_range = range(5, 10)
print("range")
print(some_range[0])
print(some_range[4])

some_string = "Georgia Tech"
print("string")
print(some_string[0])
print(some_string[8])

some_list = ["I", "like", "shorts", "they're", "comfy", "and", "easy", "to", "wear"]
print("list")
print(some_list[0])
print(some_list[4])

for i in range(5, 9):
    print("Index", i)

some_string = "Georgia Tech"
print("length test")
for i in range(0, len(some_string)):
    print(i, some_string[i])

some_list = ["I", "like", "shorts", "they're", "comfy", "and", "easy", "to", "wear"]
for i in range(0, len(some_list)):
    print(i, some_list[i])