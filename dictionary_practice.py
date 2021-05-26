person1 = {"Name": "Anudeep", "Age": "25", "Place": "Tirupati"}

print(person1["Age"])

print(person1.get("Place"))

if person1.get("Place") is None:
    print("Place of the person is not present")

print(person1.get("Place", ["America", "Australia"]))

person1["Name"] = "Anudeep Suresh"

print(person1)

#Adding new key pair value
person1["Sex"] = "Male"
person1["Hobbies"] = ["Singing", "Cricket"]

print(person1)

#Removing elements

person1.pop("Hobbies")
print(person1)

#iterating
for item in person1:
    print("Key is :" +item +" and Value is : " +person1[item])

print(person1.keys())
print(person1.items())

print(person1.popitem())

print(person1)