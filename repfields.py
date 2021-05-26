age = 26
days = 333


print("My age is " + age.__str__() + " Years")
print("My age is {0} years {1} days".format(age,days))

print("There are {0} days in {1} , {2} , {3} , {4} , {5} , {6} , {7} months".format(30, "Jan" , "Mar" , "Jun" , "Aug" , "Oct"  , "Nov", "Dec"))

print("There are {0} days in {1} , {1} , {3} , {3} , {5} , {5} , {7} months".format(30, "Jan" , "Mar" , "Jun" , "Aug" , "Oct"  , "Nov", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))