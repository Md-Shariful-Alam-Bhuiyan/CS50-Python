students = ["Hermione", "Harry", "Ron", "Draco"]

for student in students:
    print(student)

# Another implementation of for loop
for i in range(len(students)):
    print(i, students[i])

# Dictionary:
students_2 = {
    "Hermione": "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students_2["Hermione"])
print(students_2["Harry"])

# Another way of accessing dictionary with for loop
for student in students_2:
    print(student, students_2[student], sep = ", ")

#List of Dictionary
students_3 = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus": None},
]

for student in students_3:
    print(student["name"], student["house"], student["patronus"], sep=", ")
