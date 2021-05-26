available_exits = ["north","south","west","east"]

chosen_exit = ""

while chosen_exit.casefold() not in available_exits:
    chosen_exit= input("Please choose a direction :")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

print("Congrats you are out ")
