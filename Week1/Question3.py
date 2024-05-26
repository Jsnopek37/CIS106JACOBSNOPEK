def main():
  length = float(input("Enter the length of the rectangle: "))
  width = float(input("Enter the width of the rectangle: "))
  area = length * width
  circumference = 2 * length + 2 * width
  print(f"Area: {area:.2f}")
  print(f"Circumference: {circumference:.2f}")
if __name__ == "__main__":
  main()
