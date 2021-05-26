# name = "Anudeep Thota"
#
# for character in name:
#     print(character)

mystr = "990:9234&982^238 4(237!234z(sdf&"
seperators = ""

for char in mystr:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)

print(len(mystr))