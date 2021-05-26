# for i in range(11,0,-2):
#     print("value of i is {}".format(i))
#
#
# my_list = list(range(10))
#
# print(list(range(10)))
#
# even = list(range(0,10,2))
# odd = list(range(1,10,2))
#
# print(even)
# print(odd)

my_string = "abcdefghijklmnopqrstuvwxyz"

print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0,10)
print(small_decimals)

print(small_decimals.index(3))


sevens = range(7 , 100000 , 7)

x = int(input("Please enter a number less than one million "))

if x in sevens:
    print("{} is divisible by 7".format(x))
else:
    print("{} is not divisible by 7".format(x))