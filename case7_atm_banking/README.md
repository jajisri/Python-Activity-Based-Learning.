# Experiment 7 – ATM Menu-Driven Banking Simulation

**Official Case Study:** 38

## 1. Problem Statement
Develop a menu-driven ATM program that allows users to deposit money, withdraw money, check account balance, and view transaction summaries. The program must maintain the account balance, enforce withdrawal limits, and reject invalid transactions.

## 2. Objectives
- Simulate basic ATM operations.
- Maintain account balance.
- Process deposits and withdrawals.
- Enforce withdrawal limits.
- Store and display transaction history.
- Practice loops, lists, tuples, conditional statements, and operators.

## 3. Assumptions
- Initial account balance is Rs. 5,000.
- Maximum withdrawal per transaction is Rs. 10,000.
- Deposits and withdrawals must be greater than zero.
- Withdrawals cannot exceed the available balance.
- Transactions are stored using tuples inside a list.
- The program continues until the user chooses Exit.

## 4. Algorithm
1. Start.
2. Initialize balance to Rs. 5,000.
3. Create an empty transaction list.
4. Display the ATM menu.
5. Accept the user's choice.
6. If choice is 1, display balance.
7. If choice is 2, accept deposit and update balance.
8. If choice is 3, accept withdrawal and validate the amount.
9. If choice is 4, display transaction summary.
10. If choice is 5, exit the program.
11. Otherwise, display invalid choice.
12. Repeat the menu until Exit is selected.
13. Stop.

## 5. Flowchart
Start → Initialize Balance → Display Menu → Enter Choice → Check Choice → Perform Operation → Display Result → Return to Menu → Exit → Stop.

## 6. Pseudocode
```text
START
    balance = 5000
    withdrawal_limit = 10000
    transactions = empty list

    WHILE true
        Display ATM Menu
        Read choice

        IF choice == 1
            Display balance

        ELSE IF choice == 2
            Read deposit amount
            IF amount > 0
                Update balance
                Store transaction
            ELSE
                Display invalid amount
            END IF

        ELSE IF choice == 3
            Read withdrawal amount
            Validate amount and balance
            IF valid
                Update balance
                Store transaction
            ELSE
                Display error
            END IF

        ELSE IF choice == 4
            Display transaction history and balance

        ELSE IF choice == 5
            Exit loop

        ELSE
            Display invalid choice
        END IF
    END WHILE
STOP
```

## 7. Python Source Code
File: `case7_atm_banking.py`

## 8. Test Cases

| Test | Input | Expected Result |
|---|---|---|
| Balance | Choice 1 | Displays Rs. 5,000 |
| Deposit | Deposit Rs. 1,000 | Balance Rs. 6,000 |
| Withdrawal | Withdraw Rs. 2,000 | Balance Rs. 4,000 (if starting at Rs. 6,000) |
| Exceed withdrawal limit | Withdraw Rs. 12,000 | Rejected |
| Insufficient balance | Withdraw Rs. 8,000 | Rejected if balance is Rs. 5,000 |
| Invalid choice | Enter 8 | Displays invalid choice |
| Exit | Enter 5 | Exits program |

## 9. Output Screenshots
Insert screenshots showing ATM menu, successful deposit, successful withdrawal, invalid transaction, and transaction summary.

## 10. Conclusion
The ATM Banking Simulation successfully performs basic banking operations, maintains account balance, validates transactions, enforces withdrawal limits, and displays transaction history using Python.
