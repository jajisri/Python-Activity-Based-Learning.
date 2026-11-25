# Experiment 10 – Student Academic Risk Classification

**Official Case Study:** 66

## 1. Problem Statement
Combine student marks, attendance, and laboratory scores to classify students into academic risk categories, identify multiple risk factors, and generate a summary.

## 2. Objectives
- Analyze student marks, attendance, and lab scores.
- Identify low marks, low attendance, and low lab scores.
- Classify students into High, Medium, and Low risk categories.
- Generate a summary of risk categories.
- Practice lists, loops, conditionals, and operators.

## 3. Assumptions
- Marks and lab scores are out of 100.
- Attendance is represented as a percentage.
- Marks below 50 are considered low.
- Attendance below 75% is considered low.
- Lab scores below 60 are considered low.
- Two or more risk factors indicate High Risk.
- One risk factor indicates Medium Risk.
- No risk factors indicate Low Risk.

## 4. Algorithm
1. Start.
2. Store student names, marks, attendance, and lab scores in lists.
3. Initialize risk category counters.
4. Traverse each student using a loop.
5. Check marks, attendance, and lab scores.
6. Identify risk factors.
7. Classify the student based on the number of risk factors.
8. Display each student's details and risk category.
9. Display the total count of High, Medium, and Low risk students.
10. Stop.

## 5. Flowchart
Start → Store Student Data → Check Marks → Check Attendance → Check Lab Score → Count Risk Factors → Classify Risk → Display Student Report → Display Risk Summary → Stop.

## 6. Pseudocode
```text
START
    Store student names, marks, attendance, and lab scores
    Set High, Medium, Low counters to zero

    FOR each student
        Create empty risk_factors list

        IF marks < 50
            Add Low Marks
        END IF

        IF attendance < 75
            Add Low Attendance
        END IF

        IF lab score < 60
            Add Low Lab Score
        END IF

        IF risk factors >= 2
            Classify as High Risk
        ELSE IF risk factors == 1
            Classify as Medium Risk
        ELSE
            Classify as Low Risk
        END IF

        Display student report
    END FOR

    Display risk summary
STOP
```

## 7. Python Source Code
File: `case10_academic_risk.py`

## 8. Test Cases

| Student | Marks | Attendance | Lab | Expected Risk |
|---|---:|---:|---:|---|
| Ravi | 78 | 90% | 80 | Low |
| Sita | 85 | 82% | 88 | Low |
| Arjun | 42 | 60% | 45 | High |
| Priya | 55 | 72% | 58 | High |
| Kiran | 35 | 50% | 30 | High |

**Expected summary:**
- High Risk: 3
- Medium Risk: 0
- Low Risk: 2

## 9. Output Screenshots
Insert the screenshot of the Python program execution output here.

## 10. Conclusion
The program successfully classifies students based on marks, attendance, and lab scores. It identifies multiple risk factors and generates an academic risk summary using Python lists, loops, and conditional statements.
</WritingBlock}

## 4. Run the project

In your VS Code terminal, run:

```bash
python case10_academic_risk.py
```

Expected summary:

<box border radius="lg" padding={3} background="surface">
  <title size="lg">Academic Risk Summary</title>
  <row justify="between">
    <text>🔴 High Risk Students</text>
    **3**
  </row>
  <divider color="subtle"/>
  <row justify="between">
    <text>🟠 Medium Risk Students</text>
    **0**
  </row>
  <divider color="subtle"/>
  <row justify="between">
    <text>🟢 Low Risk Students</text>
    **2**
  </row>
</box>

Take the output screenshot and save it inside the Experiment 10 folder.

# 🎉 All 10 projects completed!

You have now prepared all 10 Python case studies for your ABL assignment.

Next, you should focus on:
1. Run and verify all 10 Python programs.
2. Capture output screenshots for each experiment.
3. Create proper flowchart diagrams for all 10.
4. Check all folders and README files.
5. Upload everything to your GitHub repository `Python-Activity-Based-Learning`.

If you want, I can next help you organize the **final GitHub repository structure and upload all 10 projects step by step**.