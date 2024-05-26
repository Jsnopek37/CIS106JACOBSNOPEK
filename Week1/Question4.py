def main():
  TUITION_PER_CREDIT = 250
  LAB_FEE = 100
  last_name = input("Enter your last name: ")
  credits_taken = int(input("Enter the number of credits taken: "))
  total_tuition = (credits_taken * TUITION_PER_CREDIT) + LAB_FEE
  print(f"Last Name: {last_name}")
  print(f"Total Tuition: ${total_tuition:.2f}")
if __name__ == "__main__":
  main()
