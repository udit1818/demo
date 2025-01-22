def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero!"
    else:
        return x / y

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):
        A = float(input("Enter first number: "))
        B = float(input("Enter second number: "))

        if choice == '1':
            print(A, "+", B, "=", add(A, B))

        elif choice == '2':
            print(A, "-", B, "=", subtract(A, B))

        elif choice == '3':
            print(A, "*", B, "=", multiply(A, B))

        elif choice == '4':
            print(A, "/", B, "=", divide(A, B))

    elif choice == '5':
        break

    else:
        print("Invalid input")
