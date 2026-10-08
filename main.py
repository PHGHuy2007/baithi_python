# Exercise 1
students = []
n = int(input("Enter number of student: "))
for i in range(n):
    id = input("Student ID: ")
    name = input("Student Name: ")
    score = float(input("Student Score: "))
    student = {
        "id": id,
        "name": name,
        "score": score
    }
    students.append(student)
print("\nAll students:")
for s in students:
    print(s)
highest = students[0]
for s in students:
    if s["score"] > highest["score"]:
        highest = s
print("Highest score:", highest)
total = 0
for s in students:
    total = total + s["score"]
average = total / n
print("Average score:", average)
print("Passed students:")
for s in students:
    if s["score"] >= 5:
        print(s)
