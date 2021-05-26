# name = "Norwegian Blue"
#
#
# print(name[0:6:3])
# print(name[0:6:2])
#
# number = "8,999:639'892?738.921,938"
#
# print(number[1::4])
#
#
# print(name[:6])
# print(name[3:5])
# print(name[0:9])
# print(name[:9])
#
# print(name[10:14])
# print(name[10:])
#
#
# print(name[:6] + name[6:])
# print(name[:])

# print(name)
#
# print(name[3])
# print(name[13])
# print(name[9])
# print(name[3])
# print(name[6])
# print(name[8])
#
# print()
#
# print(name[-11])
# print(name[-10])
# print(name[-5])
# print(name[-11])
# print(name[-8])
# print(name[-6])


number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

