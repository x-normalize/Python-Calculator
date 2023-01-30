import math


def calculator():
    while True:
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponent")
        print("6. Trigonometry (sin, cos, tan)")
        print("7. Logarithm (log, ln)")
        print("8. Exit")

        choice = input("Enter choice(1/2/3/4/5/6/7/8):")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1 + num2)
            elif choice == '2':
                print(num1 - num2)
            elif choice == '3':
                print(num1 * num2)
            elif choice == '4':
                print(num1 / num2)
            elif choice == '5':
                print(num1 ** num2)
        elif choice == '6':
            num1 = float(input("Enter number: "))
            print("Select operation:")
            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")
            trig_choice = input("Enter choice(1/2/3):")
            if trig_choice == '1':
                print(math.sin(num1))
            elif trig_choice == '2':
                print(math.cos(num1))
            elif trig_choice == '3':
                print(math.tan(num1))
        elif choice == '7':
            num1 = float(input("Enter number: "))
            print("Select operation:")
            print("1. Logarithm base 10")
            print("2. Natural logarithm")
            log_choice = input("Enter choice(1/2):")
            if log_choice == '1':
                print(math.log10(num1))
            elif log_choice == '2':
                print(math.log(num1))
        elif choice == '8':
            break
        else:
            print("Invalid Input")


calculator()
