def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"Discount applied! Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Final price: ${final_price:.2f}")
