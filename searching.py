shopping_list = ["Eggs","Milk","Bread","Rice","Soda","Beer","Spices"]

item_to_find = "Beer"
found_at = None

# for item in shopping_list:
#     if item == item_to_find:
#         found_at = shopping_list.index(item)
#         print(item_to_find +" is found at {} position of  List ".format(found_at))
#         break
#
#     print(item_to_find + " is not found at {} position".format(shopping_list.index(item)))
#
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
#
# print(item_to_find +" is found at {} position of  List ".format(found_at))


if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)