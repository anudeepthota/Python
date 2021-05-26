# #w is write mode
# r is read mode
# a is append mode
# f = open("testin.txt", "r")
#
# print(f.read())
#
# f.close()


# with open("testing_new.txt", "a") as f:
#     f.write("\nAppeding... This is python coding\n")
#     f.write("Appending..My name is Anudeep")
#     print()

# #Read lines and print
# with open("testing_new.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)

#write multiple lines

with open("testing_new1.txt", "w") as f:
    lines = ["Line1 Hi Hello","\n New Line2....", "\nPython is fun"]
    f.writelines(lines)