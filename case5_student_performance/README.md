# Experiment 5 – Student Performance Trend Analysis

**Official Case Study:** 17

## 1. Problem Statement
Analyze student marks across three assessments to identify performance trends and calculate average marks. Classify students based on their average performance.

## 2. Objectives
- Calculate average marks of students.
- Identify improving, declining, or stable trends.
- Classify students based on their performance.
- Practice lists, tuples, loops, conditionals, and arithmetic operations.

## 3. Assumptions
- Each student has marks from three assessments.
- Marks are out of 100.
- Trend is determined by comparing the first and third assessment.
- Average marks of 75 or above are Excellent.
- Average marks of 50 or above are Good.
- Average marks below 50 need improvement.

## 4. Algorithm
1. Start.
2. Store student names and marks.
3. Traverse each student's data using a loop.
4. Calculate average marks.
5. Compare first and third assessment marks.
6. Identify the trend.
7. Classify the student's performance.
8. Display the results.
9. Stop.

## 5. Flowchart
Start → Store Student Data → Calculate Average → Compare First and Third Marks → Identify Trend → Classify Performance → Display Results → Stop.

## 6. Pseudocode
```
START
    Store student names and marks

    FOR each student
        Calculate average marks

        IF third mark > first mark
            Display Improving
        ELSE IF third mark < first mark
            Display Declining
        ELSE
            Display Stable
        END IF

        IF average >= 75
            Display Excellent
        ELSE IF average >= 50
            Display Good
        ELSE
            Display Needs Improvement
        END IF
    END FOR
STOP
```

## 7. Python Source Code
File: `case5_student_performance.py`

## 8. Test Cases

| Student | Marks | Expected Trend | Performance |
|---|---|---|---|
| Ravi | 65, 70, 75 | Improving | Good |
| Sita | 85, 90, 95 | Improving | Excellent |
| Arjun | 40, 45, 50 | Improving | Needs Improvement |
| Priya | 55, 60, 58 | Improving | Good |

## 9. Output Screenshots
Insert screenshots of the program execution output here.

## 10. Conclusion
The program successfully calculates student averages, identifies performance trends, and classifies student performance using Python lists, tuples, loops, and conditional statements.
