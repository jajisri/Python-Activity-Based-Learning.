# ATM Menu-Driven Banking Simulation

balance = 5000
withdrawal_limit = 10000
transactions = []

while True:
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: Rs.", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid deposit amount")
        else:
            balance += amount
            transactions.append(("Deposit", amount))
            print("Deposit successful!")
            print("Updated Balance: Rs.", balance)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > withdrawal_limit:
            print("Withdrawal exceeds limit of Rs.", withdrawal_limit)

        elif amount > balance:
            print("Insufficient balance")

        else:
            balance -= amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful!")
            print("Updated Balance: Rs.", balance)

    elif choice == "4":
        print("\n===== TRANSACTION SUMMARY =====")

        if len(transactions) == 0:
            print("No transactions yet")
        else:
            for transaction_type, amount in transactions:
                print(transaction_type, "- Rs.", amount)

        print("Final Balance: Rs.", balance)

    elif choice == "5":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")