# 📱 Cool Console Calculator - Built by a Genius 😎

def print_header():
    print("=" * 40)
    print("        📟 Python Cool Calculator")
    print("=" * 40)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def get_operation():
    print("\nSelect an operation:")
    print(" ➕  Addition        (+)")
    print(" ➖  Subtraction     (-)")
    print(" ✖️  Multiplication  (*)")
    print(" ➗  Division        (/)")
    
    while True:
        op = input("Enter operation symbol: ").strip()
        if op in ('+', '-', '*', '/'):
            return op
        else:
            print("❌ Invalid operation! Choose from +, -, *, /.")

def calculate(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 == 0:
            return "⚠️ Error: Division by zero is undefined!"
        return n1 / n2

def main():
    print_header()
    
    num1 = get_number("🔢 Enter the first number: ")
    num2 = get_number("🔢 Enter the second number: ")
    operation = get_operation()
    
    print("\n🔍 Calculating...\n")
    result = calculate(num1, num2, operation)

    if isinstance(result, str):
        print(result)
    else:
        print(f"✅ Result: {num1} {operation} {num2} = {round(result, 4)}")

    print("\n✨ Thanks for using the Cool Calculator! Develped by oliver kimathi")
    print("=" * 40)

if __name__ == "__main__":
    main()
