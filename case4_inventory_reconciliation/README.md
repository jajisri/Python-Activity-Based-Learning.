# EXPERIMENT 4
## CASE STUDY 14: WAREHOUSE INVENTORY RECONCILIATION

### 1. Problem Statement
Compare opening stock, received quantities, dispatched quantities, and actual closing stock for multiple products. Detect stock discrepancies and calculate replenishment requirements.

### 2. Objectives
- To maintain product inventory records.
- To calculate expected closing stock.
- To identify stock excesses and shortages.
- To calculate reorder requirements.
- To use tuples, lists, loops, and conditional statements in Python.

### 3. Assumptions
- Product stock quantities are measured in units.
- Expected closing stock = Opening stock + Received stock − Dispatched stock.
- Actual closing stock is compared with expected closing stock.
- The minimum stock level is 50 units.
- Reorder quantity is calculated to bring stock to 50 units.

### 4. Algorithm
1. Start.
2. Store product inventory details in a list of tuples.
3. Read each product's opening stock, received stock, dispatched stock, and actual closing stock.
4. Calculate expected closing stock.
5. Compare actual closing stock with expected closing stock.
6. Identify whether stock matches, exceeds, or is short.
7. Check whether closing stock is below the minimum stock level.
8. Calculate reorder quantity if necessary.
9. Display the inventory report.
10. Stop.

### 5. Flowchart
Start → Store Inventory Data → Process Each Product → Calculate Expected Closing Stock → Compare Actual and Expected Stock → Identify Discrepancy → Check Reorder Level → Display Report → Stop.

### 6. Pseudocode
```text
START

STORE product inventory in a list of tuples

FOR each product:
    expected = opening + received - dispatched
    difference = closing - expected

    DISPLAY product details

    IF difference == 0:
        DISPLAY stock matched
    ELSE IF difference > 0:
        DISPLAY excess stock
    ELSE:
        DISPLAY stock shortage

    IF closing < 50:
        reorder = 50 - closing
        DISPLAY reorder quantity
    ELSE:
        DISPLAY no reorder required

DISPLAY report completed

STOP
```

### 7. Python Source Code
The source code is available in `case4_inventory_reconciliation.py`.

### 8. Test Cases

| Product | Opening | Received | Dispatched | Actual Closing | Expected Result |
|---|---:|---:|---:|---:|---|
| Laptop | 50 | 20 | 30 | 35 | Shortage of 5 |
| Mouse | 100 | 50 | 80 | 60 | Shortage of 10 |
| Keyboard | 75 | 25 | 40 | 50 | Shortage of 10 |

### 9. Output Screenshots
Insert screenshots of the Python source code and successful execution of the program here.

### 10. Conclusion
The program successfully reconciles warehouse stock by comparing expected and actual quantities, identifying discrepancies, and calculating replenishment requirements using Python lists, tuples, loops, and conditional statements.
