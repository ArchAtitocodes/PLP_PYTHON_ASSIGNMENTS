def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price: float, original price of the item
    - discount_percent: float, discount percentage to apply
    
    Returns:
    - float: final price after discount if discount is 20% or more
    - float: original price if discount is less than 20%
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied. Final price: Ksh{final_price:.2f}")
    else:
        print(f"No discount applied. Final price: Ksh{final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")
