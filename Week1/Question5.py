def calculate_discount(price, discount_percent):
    discount_amount = price * discount_percent
    discounted_price = price - discount_amount
    return discount_amount, discounted_price
def main():
    price = float(input("Enter the price of the item: $"))
    discount_percent = float(input("Enter the discount percent (in decimal form, e.g., 0.2 for 20%): "))
    discount_amount, discounted_price = calculate_discount(price, discount_percent)
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")
if __name__ == "__main__":
    main()
