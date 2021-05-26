name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age > 18 and age < 31:
    print("Hi {}, Welcome to the Holiday!!".format(name))
else:
    print("Hi {}, Sorry you are not eligible".format(name))