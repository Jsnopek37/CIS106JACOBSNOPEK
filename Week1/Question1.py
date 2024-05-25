def main():
  quantity = float(input("Enter the quantity: "))
  price_per_unit = float(input("Enter the price per unit: "))
  extended_price = quantity * price_per_unit
  print(f"The extended price is: ${extended_price:.2f}")

if __name__ == "__main__":
  main()
