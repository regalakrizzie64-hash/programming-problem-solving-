
print("================================")
print("     PYTHON TUTORIAL SYSTEM")
print("================================")

student_name = input("Enter your name: ")

while True:
    print("\nMAIN MENU")
    print("1. Introduction to Programming")
    print("2. Basic Syntax")
    print("3. Arithmetic Operators")
    print("4. Exit")

    choice = input("Choose lesson (1-4): ")

    if choice == "1":
        print("\nLESSON 1: INTRODUCTION TO PROGRAMMING")

        print("\nProgramming is giving instructions")
        print("to a computer to perform tasks.")

        print("\nPython is a programming language.")
        print("It is used to create different programs.")

        print("\nExample:")
        print('print("Hello, World!")')
        print("Output: Hello, World!")

        print("\nQUIZ")
        print("What is Python?")
        print("A. Programming language")
        print("B. Computer")
        print("C. Keyboard")

        answer = input("Your answer: ").upper()

        if answer == "A":
            print("Correct!")
        else:
            print("Incorrect! The answer is A.")

    elif choice == "2":
        print("\nLESSON 2: BASIC SYNTAX")

        print("\nSyntax means the rules in writing Python code.")

        print("\n1. PRINT")
        print("Used to display information.")
        print('Example: print("Hello")')

        print("\n2. VARIABLES")
        print("Used to store information.")
        print('Example: name = "Anna"')
        print("Example: age = 18")

        print("\n3. COMMENTS")
        print("Used to write notes in a program.")
        print("Example: # This is a comment")

        print("\nQUIZ")
        print("Which statement displays text?")
        print("A. input()")
        print("B. print()")
        print("C. if")

        answer = input("Your answer: ").upper()

        if answer == "B":
            print("Correct!")
        else:
            print("Incorrect! The answer is B.")

    elif choice == "3":
        print("\nLESSON 3: ARITHMETIC OPERATORS")

        num1 = 10
        num2 = 5

        print("\nFirst Number:", num1)
        print("Second Number:", num2)

        print("\nAddition (+):", num1 + num2)
        print("Subtraction (-):", num1 - num2)
        print("Multiplication (*):", num1 * num2)
        print("Division (/):", num1 / num2)
        print("Modulus (%):", num1 % num2)
        print("Floor Division (//):", num1 // num2)
        print("Exponent (**):", num1 ** num2)

        print("\nQUIZ")
        print("What is 10 + 5?")
        print("A. 10")
        print("B. 15")
        print("C. 20")

        answer = input("Your answer: ").upper()

        if answer == "B":
            print("Correct!")
        else:
            print("Incorrect! The answer is B.")

    elif choice == "4":
        print("\nThank you for using Python Tutorial!")
        print("Goodbye,", student_name)
        break

    else:
        print("\nInvalid choice! Please choose 1 to 4.")
    