string = "1234567890"

for char in string:
    print(char)

for char in iter(string):
    print(char)


cars = ["audi" , "bmw" , "jeep" , "toyota"]

my_iterator = iter(cars)

for i in range(0,len(cars)):
    next_item = next(my_iterator)
    print(next_item)


for car in cars:
    print(car)