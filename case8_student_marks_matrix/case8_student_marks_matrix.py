# Student Marks Matrix Analysis

students = ["Ravi", "Sita", "Arjun", "Priya"]
subjects = ("Maths", "Python", "English")

marks = [
    [78, 80, 65],
    [90, 88, 85],
    [45, 30, 55],
    [60, 60, 70]
]

print("===== STUDENT MARKS MATRIX ANALYSIS =====")

# Calculate student averages
student_averages = []

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    student_averages.append(average)

    print("\nStudent:", students[i])
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", round(average, 2))

# Find topper
top_index = student_averages.index(max(student_averages))

print("\nTop Performer:", students[top_index])
print("Highest Average:", round(student_averages[top_index], 2))

# Calculate subject averages
print("\n===== SUBJECT AVERAGES =====")

subject_averages = []

for j in range(len(subjects)):
    total = 0

    for i in range(len(students)):
        total += marks[i][j]

    average = total / len(students)
    subject_averages.append(average)

    print(subjects[j], "Average:", round(average, 2))

# Identify low-performing subjects
print("\n===== LOW-PERFORMING SUBJECTS =====")

found = False

for j in range(len(subjects)):
    if subject_averages[j] < 65:
        print(subjects[j], "is below 65 average marks")
        found = True

if not found:
    print("No low-performing subjects")

print("\n===== ANALYSIS COMPLETED =====")