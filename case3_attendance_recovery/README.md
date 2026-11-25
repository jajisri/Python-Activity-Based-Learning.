# EXPERIMENT 3
## CASE STUDY 12: ATTENDANCE RECOVERY COMPUTATION

### 1. Problem Statement
Calculate a student's current attendance percentage and determine the number of future classes required to reach the minimum eligibility percentage under different future attendance scenarios.

### 2. Objectives
- To calculate attendance percentages.
- To check examination eligibility.
- To use loops and conditional statements.
- To estimate attendance recovery under different future attendance rates.

### 3. Assumptions
- Minimum required attendance is 75%.
- Future attendance scenarios are 100%, 90%, and 75%.
- Future attendance patterns are simulated.
- The maximum simulation limit is 1000 future classes.
- This program is an educational simulation.

### 4. Algorithm
1. Start.
2. Input classes attended and total classes conducted.
3. Validate the attendance details.
4. Calculate the current attendance percentage.
5. Check whether the student is eligible for examination.
6. Set future attendance scenarios to 100%, 90%, and 75%.
7. For each scenario, simulate future classes using a loop.
8. Calculate the updated attendance percentage.
9. Display the number of classes required or whether the target cannot be reached.
10. Stop.

### 5. Flowchart
Start → Input Attended and Conducted Classes → Validate Inputs → Calculate Current Attendance → Check 75% Eligibility → Simulate Future Attendance Scenarios → Calculate Recovery → Display Results → Stop.

### 6. Pseudocode
```text
START
INPUT attended
INPUT conducted
SET target = 75

IF attendance inputs are invalid:
    DISPLAY invalid details
ELSE:
    CALCULATE current percentage
    DISPLAY current percentage

    CHECK examination eligibility

    SET scenarios = [100, 90, 75]

    FOR each rate in scenarios:
        SET future classes = 0

        WHILE attendance percentage < target:
            SIMULATE future attendance
            UPDATE attended and conducted classes
            INCREASE future classes

        DISPLAY recovery result

STOP
```

### 7. Python Source Code
The source code is available in `case3_attendance_recovery.py`.

### 8. Test Cases

| Attended | Conducted | Expected Result |
|---:|---:|---|
| 60 | 100 | 60% – Not eligible |
| 80 | 100 | 80% – Eligible |
| 0 | 0 | Invalid attendance details |
| 45 | 60 | 75% – Eligible |

### 9. Output Screenshots
Insert screenshots of the Python code and program execution here.

### 10. Conclusion
The program calculates attendance percentage, checks examination eligibility, and simulates attendance recovery under different future attendance scenarios using loops and conditional statements.
