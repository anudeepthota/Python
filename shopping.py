shopping_list = ["Eggs","Milk","Bread","Rice"]

# for item in shopping_list:
#     if item != "Milk":
#      print("Buy "+item)

for item in shopping_list:
    if item == "Milk":
        break
    print("Buy "+item)