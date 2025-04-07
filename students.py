import csv



# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
#     "Padma": "Ravenclaw",
# }
# for student in students:
#     print(student)


#=======================================================================#
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(type(row))
#         print(f"{row[0]} is in {row[1]}")


#====================================================================#

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",") # Hence line has only two comma sepeated value so we can unpack the list into two variable
#         # print(type(name))
#         print(f"{name} is in {house}")


#===================================================================#

# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",") # Hence line has only two comma sepeated value
#         students.append(f"{name} is in {house}")

#     for student in sorted(students):
#         print(student)

#==================================================================#

# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name":name, "house":house} # creating dictionary to enlist info into it from the variable
#         students.append(student)

#     def get_name(pupil:dict) -> str:
#         return pupil["name"]

#     for student in sorted(students, key= get_name):
#         print(f"{student['name']} is in {student['house']}")


#=========================================================================#

# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",") # Hence line has only two comma sepeated value according to the csv file so list unpacking goes here
#         student = {"name":name, "house":house}
#         students.append(student)

# # we can use lambda function instead of using any defined function like 'get_name()' above

#     for student in sorted(students, key= lambda pupil: pupil['name'] ):
#         print(f"{student['name']} is in {student['house']}")

#=============================================================================#

# Using csv library to read and write csv files
# students = []

# with open("students_2.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name":row[0],"home":row[1]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")


#============================================================================#


# Using csv library to read and write csv files and also using list unpacking

# students = []

# with open("students_2.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader: # List unpacking actives here
#         students.append({"name":name,"home":home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")


#=====================================================================#

students = []

with open("students_3.csv") as file:
    reader = csv.DictReader(file) # DictReader returns dictionary for each line or row of a csv file
    print(reader)
    for row in reader: #
        print(row)
        students.append({"name":row["name"],"home":row["home"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")


#==========================================================================#

# name = input("What's your name ?")
# home = input("Where's your home ?")

# with open("students_3.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home]) # writing row as a list of all the values that we want to put from left to right

#===========================================================================#

# write Via Dictionary Writer:

# name = input("What's your name ?")
# home = input("Where's your home ?")

# with open("students_3.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name","home"]) # fieldsname has to be a list of ordered column name in string Dthat exists in the csv file
#     writer.writerow({"name":name, "home":home}) # writerow as a dictionary format



