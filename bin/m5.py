import cal1

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")

    while True:
        choice = input("Enter your choice (1-6) or 'q' to quit: ")
        
        if choice.lower() == 'q':
            break
        
        try:
            choice = int(choice)
            if choice < 1 or choice > 6:
                print("Invalid choice. Please choose a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            print(f"{x} + {y} = {cal1.add1(x, y)}")
        elif choice == 2:
            print(f"{x} - {y} = {cal1.sub1(x, y)}")
        elif choice == 3:
            print(f"{x} * {y} = {cal1.mul1(x, y)}")
        elif choice == 4:
            result = cal1.div1(x, y)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{x} / {y} = {result}")
        elif choice == 5:
            result = cal1.mod1(x, y)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{x} % {y} = {result}")
        elif choice == 6:
            print(f"{x} ^ {y} = {cal1.pow1(x, y)}")
