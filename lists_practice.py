languages = ["Java", "Python", "C++", ".NET"]

print(languages[-1])


for language in languages:
    print("The name of the Language is :" + language)

print(languages[0:4])


print(languages[:])


languages[0:3] = ["C","GO"]


print(languages)


languages.append("Kotlin")

print("Kotlin" in languages)


languages.insert(0, "C#")

print(languages)


languages.remove("C#")
print(languages)

#NestedList

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][0])
n_list[1].append(3)
print(n_list)


del n_list[1][2]

print(n_list)