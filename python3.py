original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount_amount = (discount_percentage / 100) * original_price
final_price = original_price - discount_amount

print(f"Final price after discount: {final_price}")
