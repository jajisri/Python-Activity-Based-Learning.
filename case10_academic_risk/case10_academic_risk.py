# Student Academic Risk Classification

students = ["Ravi", "Sita", "Arjun", "Priya", "Kiran"]

marks = [78, 85, 42, 55, 35]
attendance = [90, 82, 60, 72, 50]
lab_scores = [80, 88, 45, 58, 30]

high_risk = 0
medium_risk = 0
low_risk = 0

print("===== STUDENT ACADEMIC RISK REPORT =====")

for i in range(len(students)):
    risk_factors = []

    if marks[i] < 50:
        risk_factors.append("Low Marks")

    if attendance[i] < 75:
        risk_factors.append("Low Attendance")

    if lab_scores[i] < 60:
        risk_factors.append("Low Lab Score")

    # Risk classification
    if len(risk_factors) >= 2:
        category = "High Risk"
        high_risk += 1

    elif len(risk_factors) == 1:
        category = "Medium Risk"
        medium_risk += 1

    else:
        category = "Low Risk"
        low_risk += 1

    print("\nStudent:", students[i])
    print("Marks:", marks[i])
    print("Attendance:", attendance[i], "%")
    print("Lab Score:", lab_scores[i])

    if risk_factors:
        print("Risk Factors:", ", ".join(risk_factors))
    else:
        print("Risk Factors: None")

    print("Risk Category:", category)

print("\n===== RISK SUMMARY =====")
print("High Risk Students:", high_risk)
print("Medium Risk Students:", medium_risk)
print("Low Risk Students:", low_risk)

print("\n===== ANALYSIS COMPLETED =====")