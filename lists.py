# ipAddress = input("Please enter your IP Address : ")
#
# print(ipAddress.count("."))

states_List = ["texas" , "california" , "newyork" , "florida"]
states_List.append("colorado")

for state in states_List:
    print("The state is " + state)

even = ["2","4","6","8"]
odd = ["1","3","5","7"]

numbers = even + odd
#numbers.sort()

numbers_in_order =  sorted(numbers)
print(numbers_in_order)


if numbers_in_order == sorted(numbers):
    print("numbers are sorted")
else:
    print("numbers are not sorted")

print(len(even))

