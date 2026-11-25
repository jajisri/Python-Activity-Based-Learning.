# Experiment 6 – Repeated Transaction Detection

**Official Case Study:** 28

## 1. Problem Statement
Process transaction IDs and amounts stored in a list, detect duplicate transactions, identify transactions exceeding a specified amount limit, and generate a list of suspicious transactions.

## 2. Objectives
- Detect duplicate transaction IDs.
- Identify transactions above a given amount limit.
- Store suspicious transactions in a separate list.
- Practice lists, tuples, loops, conditionals, and operators.

## 3. Assumptions
- Transactions are stored as tuples containing ID and amount.
- The amount threshold is Rs. 10,000.
- A transaction is suspicious if its ID is repeated or its amount exceeds Rs. 10,000.
- Both conditions may apply to the same transaction.

## 4. Algorithm
1. Start.
2. Store transaction IDs and amounts in a list.
3. Create an empty list to store previously seen IDs.
4. Create an empty suspicious transactions list.
5. Read each transaction using a loop.
6. Check if the transaction ID already exists.
7. Check if the amount exceeds Rs. 10,000.
8. If either condition is true, mark the transaction as suspicious.
9. Display the audit report.
10. Stop.

## 5. Flowchart
Start → Store Transactions → Read Transaction → Check Duplicate ID → Check Amount Limit → Mark Suspicious or Normal → Display Report → Stop.

## 6. Pseudocode
```text
START
    Store transactions
    Create seen_ids list
    Create suspicious list

    FOR each transaction
        Create empty reasons list

        IF ID exists in seen_ids
            Add Duplicate Transaction to reasons
        ELSE
            Add ID to seen_ids
        END IF

        IF amount > threshold
            Add Amount Above Limit to reasons
        END IF

        IF reasons is not empty
            Add transaction to suspicious list
        END IF

        Display transaction status
    END FOR

    Display suspicious transactions
    Display total count
STOP
```

## 7. Python Source Code
File: `case6_repeated_transaction.py`

## 8. Test Cases

| Transaction ID | Amount (₹) | Expected Result |
|---|---:|---|
| T101 | 5,000 | Normal |
| T102 | 12,000 | Suspicious – Amount Above Limit |
| T103 | 3,000 | Normal |
| T101 | 5,000 | Suspicious – Duplicate |
| T104 | 15,000 | Suspicious – Amount Above Limit |
| T102 | 12,000 | Suspicious – Duplicate and Amount Above Limit |

## 9. Output Screenshots
Insert the screenshot of the Python program execution output here.

## 10. Conclusion
The program detects repeated transaction IDs and high-value transactions using Python lists, tuples, loops, and conditional statements. It generates a report of suspicious transactions for audit purposes.
