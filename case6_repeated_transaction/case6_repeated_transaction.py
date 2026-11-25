# Repeated Transaction Detection

transactions = [
    ("T101", 5000),
    ("T102", 12000),
    ("T103", 3000),
    ("T101", 5000),
    ("T104", 15000),
    ("T102", 12000)
]

threshold = 10000
seen_ids = []
suspicious = []

print("===== TRANSACTION AUDIT REPORT =====")

for transaction_id, amount in transactions:
    reasons = []

    # Check duplicate transaction ID
    if transaction_id in seen_ids:
        reasons.append("Duplicate Transaction")
    else:
        seen_ids.append(transaction_id)

    # Check transaction amount threshold
    if amount > threshold:
        reasons.append("Amount Above Limit")

    if reasons:
        suspicious.append((transaction_id, amount, reasons))

    print("\nTransaction ID:", transaction_id)
    print("Amount: Rs.", amount)

    if reasons:
        print("Status: Suspicious")
        print("Reason:", ", ".join(reasons))
    else:
        print("Status: Normal")

print("\n===== SUSPICIOUS TRANSACTIONS =====")

for transaction_id, amount, reasons in suspicious:
    print(transaction_id, "| Rs.", amount, "|", ", ".join(reasons))

print("\nTotal Transactions:", len(transactions))
print("Suspicious Transactions:", len(suspicious))
print("===== AUDIT COMPLETED =====")