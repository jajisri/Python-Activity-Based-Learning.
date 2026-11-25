# Experiment 9 – Tuple-Based Employee Shift Conflict Detection

**Official Case Study:** 48

## 1. Problem Statement
Represent employee shifts using tuples, compare shift time intervals, detect overlapping assignments, and identify employees having conflicting schedules.

## 2. Objectives
- Store employee shift details using tuples.
- Compare time intervals.
- Detect overlapping shifts for the same employee.
- Display conflicting shift assignments.
- Practice tuples, lists, loops, and conditional statements.

## 3. Assumptions
- Shift details contain employee name, start time, and end time.
- Time is represented in 24-hour format using whole hours.
- Two shifts conflict when they overlap for the same employee.
- Shifts that meet exactly at the same ending and starting time are not considered overlapping.
- Sample shift records are used for analysis.

## 4. Algorithm
1. Start.
2. Store employee shift records as tuples inside a list.
3. Display all shift records.
4. Compare each shift with the remaining shifts using nested loops.
5. Check if the employee names are the same.
6. Check if the time intervals overlap.
7. If both conditions are true, record the conflict.
8. Display all conflicts and total conflict count.
9. Stop.

## 5. Flowchart
Start → Store Employee Shifts → Display Schedule → Compare Shift Pairs → Same Employee? → Check Time Overlap → Record Conflict → Display Results → Stop.

## 6. Pseudocode
```text
START
    Store employee shifts in a list of tuples
    Create empty conflicts list

    FOR i from 0 to number of shifts
        FOR j from i+1 to number of shifts

            Extract employee names and times

            IF employee names are same
                IF start1 < end2 AND start2 < end1
                    Record conflict
                    Display conflict
                END IF
            END IF

        END FOR
    END FOR

    Display total conflicts
STOP
```

## 7. Python Source Code
File: `case9_shift_conflict.py`

## 8. Test Cases

| Employee | Shift 1 | Shift 2 | Expected Result |
|---|---|---|---|
| Ravi | 9–13 | 12–16 | Conflict |
| Sita | 9–14 | 15–19 | No conflict |
| Ravi | 16–20 | 12–16 | No conflict (touching boundary) |
| Arjun | 10–15 | No other shift | No conflict |

## 9. Output Screenshots
Insert the screenshot of the program execution output here.

## 10. Conclusion
The program successfully detects employee shift conflicts by comparing time intervals using tuples, lists, nested loops, and conditional statements.
