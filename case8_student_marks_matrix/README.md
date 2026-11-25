# Experiment 8 – Student Marks Matrix Analysis

**Official Case Study:** 42

## 1. Problem Statement
Analyze student marks stored in a nested list (matrix). Calculate student-wise averages, subject-wise averages, identify top performers, and detect subjects with low average marks.

## 2. Objectives
- Store student marks using nested lists.
- Calculate row-wise averages.
- Calculate column-wise averages.
- Identify the top-performing student.
- Identify subjects with average marks below a specified limit.
- Practice nested lists, loops, tuples, and conditional statements.

## 3. Assumptions
- Four students and three subjects are considered.
- Marks are out of 100.
- Student marks are stored in a nested list.
- Subject names are stored in a tuple.
- A subject average below 65 is considered low-performing.

## 4. Algorithm
1. Start.
2. Store student names, subjects, and marks.
3. Calculate each student's total and average.
4. Store student averages in a list.
5. Find the highest average and identify the top performer.
6. Calculate the average of each subject.
7. Identify subjects with averages below 65.
8. Display all analysis results.
9. Stop.

## 5. Flowchart
Start → Store Student Marks Matrix → Calculate Student Averages → Find Top Performer → Calculate Subject Averages → Check Low-Performing Subjects → Display Report → Stop.

## 6. Pseudocode
```text
START
    Store student names
    Store subject names
    Store marks matrix

    FOR each student
        Calculate total marks
        Calculate average
        Store average
        Display student results
    END FOR

    Find maximum student average
    Display top performer

    FOR each subject
        Calculate subject total
        Calculate subject average
        Display average

        IF subject average < 65
            Display low-performing subject
        END IF
    END FOR
STOP
```

## 7. Python Source Code
File: `case8_student_marks_matrix.py`

## 8. Test Cases

| Student | Maths | Python | English | Expected |
|---|---:|---:|---:|---|
| Ravi | 78 | 80 | 65 | Average 74.33 |
| Sita | 90 | 88 | 85 | Top performer, average 87.67 |
| Arjun | 45 | 30 | 55 | Average 43.33 |
| Priya | 60 | 60 | 70 | Average 63.33 |

**Expected subject averages:**
- Maths: 68.25
- Python: 64.50
- English: 68.75

Python should be identified as a low-performing subject.

## 9. Output Screenshots
Insert a screenshot of the Python execution output here.

## 10. Conclusion
The program successfully analyzes student marks using nested lists. It calculates student and subject averages, identifies the top performer, and detects low-performing subjects using Python loops and conditional statements.
</WritingBlock}

## 4. Run the project

In your VS Code terminal, run:

```bash
python case8_student_marks_matrix.py
```

Expected results:

- **Top performer:** Sita
- **Highest average:** 87.67
- **Low-performing subject:** Python (64.50)

Take your output screenshot and save it inside the Experiment 8 folder.

After this, we'll do **Experiment 9 – Tuple-Based Employee Shift Conflict Detection**.