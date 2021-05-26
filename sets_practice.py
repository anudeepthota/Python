#No duplicate items

animals = {'dog', 'cat', 'lion', 'lion'}

print(animals)


test_set = set(('dog', 'cat', 'cheetah', 'lion', 'lion'))

print(test_set)

#adding
animals.add("Monkey")

print(animals)


wild_animals = ['Tiger', 'Crocodile', 'Snake']

#update
animals.update(wild_animals, ["White Tiger"])

print(animals)

#remove
animals.discard("Feeret")

print(animals)


#clear

#animals.clear()

#print(animals)


#check presence
if("Tiger"  in animals):
    print("Yes tiger is present")


#loops

for animal in animals:
    print(animal)

#union

animals1 = {'Tiger', 'Crocodile', 'Snake'}

animals2 = {'dog', 'cat', 'lion', 'Tiger'}


#new_animals = animals1.union(animals2)

new_animals = animals1 | animals2


print(new_animals)

#intersection


#new_animals = animals1.intersection(animals2)

new_animals = animals1 & animals2

print(new_animals)

#set difference
#print(animals2 - animals1)

print(animals2.difference(animals1))


