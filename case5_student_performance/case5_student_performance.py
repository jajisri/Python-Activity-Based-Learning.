# Student Performance Trend Analysis

students = [
    ("Ravi", [65, 70, 75]),
    ("Sita", [85, 90, 95]),
    ("Arjun", [40, 45, 50]),
    ("Priya", [55, 60, 58]),
]

print("===== STUDENT PERFORMANCE TREND =====")

for name, marks in students:
    average = sum(marks) / len(marks)

    print("\nStudent:", name)
    print("Marks:", marks)
    print("Average:", round(average, 2))

    if marks[2] > marks[0]:
        print("Trend: Improving")
    elif marks[2] < marks[0]:
        print("Trend: Declining")
    else:
        print("Trend: Stable")

    if average >= 75:
        print("Performance: Excellent")
    elif average >= 50:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

print("\n===== ANALYSIS COMPLETED =====")