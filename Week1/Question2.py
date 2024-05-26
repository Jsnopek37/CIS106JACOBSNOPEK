def main():
  last_name = input("Enter your last name: ")
  hours_worked = float(input("Enter the number of hours worked: "))
  pay_rate = float(input("Enter your pay rate: "))
  gross_pay = hours_worked * pay_rate
  print(f"Last Name: {last_name}")
  print(f"Gross Pay: ${gross_pay:.2f}")
if __name__ == "__main__":
  main()
