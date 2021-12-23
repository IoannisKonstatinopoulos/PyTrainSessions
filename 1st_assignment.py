#Exercise #2

print("Exercise #1\n")
listFoods = ["pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"]
items = 0
for food in listFoods:
    print(food)
    items += 1
print("Total number of items = ",items)

#Exercise #2
print("\nExercise #2\n")

letters = ['a','e','i','o','u']
souma_letters = [0,0,0,0,0]
for food in listFoods:
    for letter in range(len(souma_letters)):
        souma_letters[letter] += food.count(letters[letter])

for letter in range(len(letters)):
    print("The letter ",letters[letter]," appears ",souma_letters[letter],"times")

#Exercise #3

print("\nExercise #3\n")

listFoodsReversed = [i[::-1] for i in listFoods]
for reversedFood in listFoodsReversed:
    print(reversedFood)

#Exercise #4

print("\nExercise #4\n")
diction = {}
for key in range(len(letters)):
    diction[letters[key]] = souma_letters[key]
print(diction)
