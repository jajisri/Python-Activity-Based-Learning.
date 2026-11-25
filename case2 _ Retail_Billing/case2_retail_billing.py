
# Retail Billing with Multiple Discount Rules

products = []
total_bill = 0

n = int(input("Enter number of products: "))

# Collect product details
for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    category = input("Enter category (food/clothing/electronics/other): ").lower()

    products.append((name, price, quantity, category))

print("\n========== RETAIL INVOICE ==========")

# Process each product
for name, price, quantity, category in products:

    amount = price * quantity

    # Category-based tax
    if category == "food":
        tax_rate = 5
    elif category == "clothing":
        tax_rate = 12
    elif category == "electronics":
        tax_rate = 18
    else:
        tax_rate = 10

    tax = amount * tax_rate / 100

    # Discount rules
    if amount >= 5000:
        discount = amount * 20 / 100
    elif amount >= 2000:
        discount = amount * 10 / 100
    elif amount >= 1000:
        discount = amount * 5 / 100
    else:
        discount = 0

    # Maximum discount limit
    if discount > 1000:
        discount = 1000

    final_amount = amount + tax - discount
    total_bill += final_amount

    print("\nProduct:", name)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Subtotal:", amount)
    print("Tax:", tax, "%")
    print("Discount:", discount)
    print("Amount:", round(final_amount, 2))

print("\n==================================")
print("TOTAL BILL: Rs.", round(total_bill, 2))
print("==================================")
