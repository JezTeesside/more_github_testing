students = {"John":38, "Ron":68, "Maria":78, "Oxana":45, "Sam":32}
pass_students = {}
fail_students = {}
for student,marks in students.items():
    if(marks >= 40):
        pass_students[student] = marks
    else:
        fail_students[student] = marks
print("Summary")
print("All students: ", list(students.keys()))
print("Pass students: ", list(pass_students.keys()))
print("Fail students: ", list(fail_students.keys()))
