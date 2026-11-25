# EXPERIMENT 1
## CASE STUDY 2: PROGRESSIVE ELECTRICITY BILLING

### 1. Problem Statement
Calculate an electricity bill based on the number of units consumed using different electricity billing slabs.

### 2. Objectives
- To calculate electricity charges based on consumption.
- To use conditional statements in Python.
- To understand progressive billing.
- To validate negative unit inputs.

### 3. Assumptions
- First 100 units: ₹2 per unit.
- 101–200 units: ₹3 per unit for units above 100.
- Above 200 units: ₹5 per unit for units above 200.
- No fixed charges or additional fees are considered.

### 4. Algorithm
1. Start.
2. Input electricity units.
3. Check whether units are negative.
4. If negative, display invalid units.
5. If units are up to 100, calculate at ₹2 per unit.
6. If units are up to 200, calculate the first 100 at ₹2 and remaining at ₹3.
7. Otherwise, calculate the first 100 at ₹2, next 100 at ₹3, and remaining at ₹5.
8. Display the electricity bill.
9. Stop.

### 5. Flowchart
Start → Input Units → Check Units → Apply Billing Slab → Calculate Bill → Display Bill → Stop.

### 6. Pseudocode
```text
START
INPUT units

IF units < 0:
    PRINT "Invalid units"
ELSE IF units <= 100:
    bill = units * 2
ELSE IF units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
ELSE:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

IF units >= 0:
    PRINT bill

STOP
```

### 7. Python Source Code
The Python source code is saved in `case1_electricity_bill.py`.

### 8. Test Cases

| Units | Expected Output |
|---:|---:|
| 80 | ₹160 |
| 150 | ₹350 |
| 250 | ₹750 |
| -5 | Invalid units |

### 9. Output Screenshots
Insert the screenshots of the Python code and program outputs in this section.

### 10. Conclusion
The program calculates electricity bills using progressive billing slabs and conditional statements. It successfully handles different consumption levels and invalid negative inputs.
