numbers = [1,45,31,60,12]

for number in numbers:
    if number % 8 == 0 :
        print("The numbers are unacceptable :")
        break
else:
    print("All those numbers are fine")