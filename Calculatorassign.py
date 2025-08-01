# Simple Calculator Program

def main():
    # Welcome message
    print("\nWelcome to the Python Calculator!")
    print("This program performs basic operations on two numbers.")
    print("Available operations: + (addition), - (subtraction), * (multiplication), / (division)\n")
    
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform the calculation
        if operation == '+':
            result = num1 + num2
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("\nError: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} {operation} {num2} = {result}")
        else:
            print("\nInvalid operation! Please enter one of: +, -, *, /")
    
    except ValueError:
        print("\nError: Please enter valid numbers!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    
    print("\nThank you for using the calculator!")

# Run the program
if __name__ == "__main__":
    main()