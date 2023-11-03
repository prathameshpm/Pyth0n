"""
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])
"""

"""
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
"""

"""
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(students[i])
"""

"""
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
"""

"""
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron":  "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
"""

"""
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron":  "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student)
"""

"""
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron":  "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student])
"""

"""
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron":  "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=", ")
"""


students = [
    {   "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {   "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {   "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell Terrier"
    },
    {   "name": "Draco",
        "house": "Slytherin",
        "patronus": None
    }
]

for student in students:
    print(student["name"], student["house"], 
    student["patronus"], sep=", ")