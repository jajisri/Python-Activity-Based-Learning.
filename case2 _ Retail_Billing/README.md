# EXPERIMENT 2
## CASE STUDY 7: RETAIL BILLING WITH MULTIPLE DISCOUNT RULES

### 1. Problem Statement
Develop a Python program to process multiple products, calculate their subtotal, apply category-specific taxes and threshold-based discounts, limit the maximum discount, and generate an itemized retail bill.

### 2. Objectives
- To calculate product cost based on price and quantity.
- To apply taxes based on product categories.
- To apply discounts based on purchase amounts.
- To limit the maximum discount.
- To generate an itemized invoice using Python.

### 3. Assumptions
- Food products have a 5% tax.
- Clothing products have a 12% tax.
- Electronics products have an 18% tax.
- Other categories have a 10% tax.
- Purchases of ₹5,000 or more receive a 20% discount.
- Purchases of ₹2,000 or more receive a 10% discount.
- Purchases of ₹1,000 or more receive a 5% discount.
- Purchases below ₹1,000 receive no discount.
- The maximum discount per product is ₹1,000.

### 4. Algorithm
1. Start.
2. Input the number of products.
3. Input product name, price, quantity and category.
4. Store the product details in a list of tuples.
5. Calculate the subtotal using price × quantity.
6. Apply tax based on product category.
7. Apply discount based on subtotal.
8. Limit the discount to ₹1,000.
9. Calculate the final amount for each product.
10. Add each final amount to the total bill.
11. Display the itemized invoice.
12. Stop.

### 5. Flowchart

Start → Input Number of Products → Enter Product Details → Store in List → Calculate Subtotal → Calculate Category Tax → Apply Discount → Check Maximum Discount → Calculate Final Amount → Display Item Details → Repeat for Remaining Products → Display Total Bill → Stop.

### 6. Pseudocode

```text
START
INPUT number_of_products
CREATE empty product list
SET total_bill = 0

FOR each product:
    INPUT name, price, quantity, category
    STORE details in list

FOR each product in list:
    subtotal = price * quantity

    IF category is food:
        tax_rate = 5
    ELSE IF category is clothing:
        tax_rate = 12
    ELSE IF category is electronics:
        tax_rate = 18
    ELSE:
        tax_rate = 10

    CALCULATE tax

    IF subtotal >= 5000:
        discount = 20% of subtotal
    ELSE IF subtotal >= 2000:
        discount = 10% of subtotal
    ELSE IF subtotal >= 1000:
        discount = 5% of subtotal
    ELSE:
        discount = 0

    IF discount > 1000:
        discount = 1000

    final_amount = subtotal + tax - discount
    ADD final_amount to total_bill
    DISPLAY product invoice

DISPLAY total_bill
STOP
```

### 7. Python Source Code
The source code is available in the file `case2_retail_billing.py` in this repository.

### 8. Test Cases

| Test | Product | Price | Quantity | Category | Expected Final Amount |
|---|---|---:|---:|---|---:|
| 1 | Laptop | 50000 | 1 | Electronics | ₹58,000 |
| 2 | Shirt | 1000 | 2 | Clothing | ₹2,040 |
| 3 | Rice | 300 | 2 | Food | ₹630 |

**Expected Total Bill: ₹60,670**

### 9. Output Screenshots
Insert the screenshots of the Python source code and successful program execution here.

### 10. Conclusion
The program successfully generates a retail invoice for multiple products by calculating subtotals, category-specific taxes, threshold discounts and maximum discount limits. It demonstrates the use of lists, tuples, loops, conditional statements and arithmetic operators in Python.
