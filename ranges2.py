# decimals = range(0,100)
#
# my_range = decimals[3:40:3]
# print(range(0,5,2) == range(0,6,2))
# print(list(range(0,5,2)))
#
# print("=" * 30)
#
# print(list(range(0,6,2)))




o = range(0, 100, 4)
print(list(o))
p = o[::5]
print(list(p))
for i in p:
    print(i)

my = range(0,50,10)

me = my[::-1]

for i in me:
    print(i)
