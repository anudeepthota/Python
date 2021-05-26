new_tup = (1,2,3,4)

print(new_tup)

#Nested Tuples
nested_tuples = (2 , "Anudeep" , [3,5,7], (9,8,7))

nested_tuples[2][1] = 4

print(nested_tuples)

#packedtuple
packed_tuple = 3, "Anudeep", [3,5,6,7,8]

a , b , c  = packed_tuple

print(b)


test_tuple = (3,)


#del packed_tuple



print(type(test_tuple))


for item in packed_tuple:
    if(type(item) is list):
        print("List is " + str(item))
    else:
     print("Item in tuple : " + str(item))


#UPACKING TUPLES

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#multiply tuples

names = ("Anudeep", "Nihitha", "Madhavi")
mytuple = names * 2

print(mytuple)


#count

examples = (1,1,1,2)

print(examples.count(1))



