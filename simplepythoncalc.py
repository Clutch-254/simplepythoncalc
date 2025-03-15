import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def modulus(x, y):
    return x % y

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def logarithm(x):
    if x <= 0:
        return "Error: Logarithm is only defined for positive numbers."
    return math.log10(x)

def display_menu():
    print("\nPython Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Square")
    print("7. Cube")
    print("8. Logarithm (base 10)")
    print("9. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-9): ")

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
        elif choice in ['6', '7', '8']:
            num1 = get_number("Enter the number: ")
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {modulus(num1, num2)}")
        elif choice == '6':
            print(f"Result: {square(num1)}")
        elif choice == '7':
            print(f"Result: {cube(num1)}")
        elif choice == '8':
            print(f"Result: {logarithm(num1)}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()