
# List of 10 student dictionaries
students = [
    {"studentname": "Tushar", "age": 25, "rollnumber": 179},
    {"studentname": "Aman", "age": 22, "rollnumber": 101},
    {"studentname": "Riya", "age": 21, "rollnumber": 102},
    {"studentname": "Neha", "age": 23, "rollnumber": 103},
    {"studentname": "Rohit", "age": 24, "rollnumber": 104},
    {"studentname": "Suman", "age": 22, "rollnumber": 105},
    {"studentname": "Karan", "age": 23, "rollnumber": 106},
    {"studentname": "Priya", "age": 21, "rollnumber": 107},
    {"studentname": "Ankit", "age": 24, "rollnumber": 108},
    {"studentname": "Meena", "age": 22, "rollnumber": 109}
]
for student in students:
    print(f"{student['studentname']} {student['age']}, {student['rollnumber']}")