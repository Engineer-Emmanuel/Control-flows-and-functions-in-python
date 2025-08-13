def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount.
    Apply discount only if discount_percent is 20 or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount)

# Print the result
if discount >= 20:
    print(f"Discount applied. The final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")