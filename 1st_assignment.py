#Exercise #2

print("Exercise #1\n")
list = ["pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"]
items = 0
for food in list:
    print(food)
    items += 1
print("Total number of items = ",items, "\n")

#Exercise #2
print("Exercise #2\n")

letters = ['a','e','i','o','u']
souma_letters = [0,0,0,0,0]
for food in list:
    for letter in range(len(souma_letters)):
        souma_letters[letter] += food.count(letters[letter])

for letter in range(len(souma_letters)):
    print("The letter ",letters[letter]," appears ",souma_letters[letter],"times")

#Exercise #3

print("\n#Exercise #3\n")
def reverse_item(x):
    return x[::-1]
for food in list:
    print(reverse_item(food))

#Exercise #4

print("\n#Exercise #4\n")
diction = {}
for key in range(len(letters)):
    diction[letters[key]] = souma_letters[key]
print(diction)