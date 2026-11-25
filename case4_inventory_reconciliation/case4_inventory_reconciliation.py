
# Warehouse Inventory Reconciliation

products = [
    ("Laptop", 50, 20, 30, 35),
    ("Mouse", 100, 50, 80, 60),
    ("Keyboard", 75, 25, 40, 50),
]

print("===== WAREHOUSE INVENTORY REPORT =====")

for product, opening, received, dispatched, closing in products:

    expected = opening + received - dispatched
    difference = closing - expected

    print("\nProduct:", product)
    print("Opening Stock:", opening)
    print("Received Stock:", received)
    print("Dispatched Stock:", dispatched)
    print("Actual Closing Stock:", closing)
    print("Expected Closing Stock:", expected)

    if difference == 0:
        print("Status: Stock Matched")
    elif difference > 0:
        print("Status: Excess Stock =", difference)
    else:
        print("Status: Stock Shortage =", abs(difference))

    if closing < 50:
        reorder = 50 - closing
        print("Reorder Required:", reorder, "units")
    else:
        print("Reorder Required: No")

print("\n===== REPORT COMPLETED =====")
