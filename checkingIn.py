parrot = "Norwegian Blue"

letter = input("Enter a character:")

if(letter in parrot):
    print("{} is present in {}".format(letter,parrot))
else:
    print("{} is not present in {}".format(letter,parrot))