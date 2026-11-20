
# ==========================================
#       PYTHON TUTORIAL SYSTEM
#       FINAL PROJECT
# ==========================================

# Display the title of the program
print("================================")
print("     PYTHON TUTORIAL SYSTEM")
print("================================")

# Ask the student to enter their name
student_name = input("Enter your name: ")

# Repeat the main menu until the student chooses Exit
while True:

    # Display the main menu
    print("\nMAIN MENU")
    print("1. Introduction to Programming")
    print("2. Basic Syntax")
    print("3. Arithmetic Operators")
    print("4. Basic Input and Output")
    print("5. Conditional Statements")
    print("6. Logical Operators")
    print("7. Iteration and Loops")
    print("8. Exit")

    # Ask the student to choose a lesson
    choice = input("Choose lesson (1-8): ")

    # ==========================================
    # LESSON 1: INTRODUCTION TO PROGRAMMING
    # ==========================================

    # Check if the student chooses Lesson 1
    if choice == "1":

        # Display Lesson 1
        print("\nLESSON 1: INTRODUCTION TO PROGRAMMING")

        # Explain the meaning of programming
        print("\nProgramming is giving instructions")
        print("to a computer to perform tasks.")

        # Introduce the Python programming language
        print("\nPython is a programming language.")
        print("It is used to create different programs.")

        # Show an example of a Python print statement
        print("\nExample:")
        print('print("Hello, World!")')
        print("Output: Hello, World!")

        # Display the quiz for Lesson 1
        print("\nQUIZ")
        print("What is Python?")
        print("A. Programming language")
        print("B. Computer")
        print("C. Keyboard")

        # Get the student's answer and convert it to uppercase
        answer = input("Your answer: ").upper()

        # Check if the answer is correct
        if answer == "A":
            print("Correct!")
        else:
            print("Incorrect! The answer is A.")

    # ==========================================
    # LESSON 2: BASIC SYNTAX
    # ==========================================

    # Check if the student chooses Lesson 2
    elif choice == "2":

        # Display Lesson 2
        print("\nLESSON 2: BASIC SYNTAX")

        # Explain the meaning of syntax
        print("\nSyntax means the rules in writing Python code.")

        # Explain the print statement
        print("\n1. PRINT")
        print("Used to display information.")
        print('Example: print("Hello")')

        # Explain variables and show examples
        print("\n2. VARIABLES")
        print("Used to store information.")
        print('Example: name = "Anna"')
        print("Example: age = 18")

        # Explain comments and show an example
        print("\n3. COMMENTS")
        print("Used to write notes in a program.")
        print("Example: # This is a comment")

        # Display the quiz for Lesson 2
        print("\nQUIZ")
        print("Which statement displays text?")
        print("A. input()")
        print("B. print()")
        print("C. if")

        # Get the student's answer and convert it to uppercase
        answer = input("Your answer: ").upper()

        # Check if the answer is correct
        if answer == "B":
            print("Correct!")
        else:
            print("Incorrect! The answer is B.")

    # ==========================================
    # LESSON 3: ARITHMETIC OPERATORS
    # ==========================================

    # Check if the student chooses Lesson 3
    elif choice == "3":

        # Display Lesson 3
        print("\nLESSON 3: ARITHMETIC OPERATORS")

        # Assign values to the two number variables
        num1 = 10
        num2 = 5

        # Display the two numbers
        print("\nFirst Number:", num1)
        print("Second Number:", num2)

        # Demonstrate different arithmetic operations
        print("\nAddition (+):", num1 + num2)
        print("Subtraction (-):", num1 - num2)
        print("Multiplication (*):", num1 * num2)
        print("Division (/):", num1 / num2)
        print("Modulus (%):", num1 % num2)
        print("Floor Division (//):", num1 // num2)
        print("Exponent (**):", num1 ** num2)

        # Display the quiz for Lesson 3
        print("\nQUIZ")
        print("What is 10 + 5?")
        print("A. 10")
        print("B. 15")
        print("C. 20")

        # Get the student's answer and convert it to uppercase
        answer = input("Your answer: ").upper()

        # Check if the answer is correct
        if answer == "B":
            print("Correct!")
        else:
            print("Incorrect! The answer is B.")

    # ==========================================
    # LESSON 4: BASIC INPUT AND OUTPUT
    # ==========================================

    # Check if the student chooses Lesson 4
    elif choice == "4":

        # Display Lesson 4
        print("\nLESSON 4: BASIC INPUT AND OUTPUT")

        # Explain input and output
        print("\nINPUT allows the user to enter information.")
        print("OUTPUT displays information on the screen.")

        # Show an example of input and output
        print("\nExample:")
        print('name = input("Enter your name: ")')
        print('print("Hello", name)')

        # Demonstrate input and output
        print("\nTRY IT YOURSELF")

        name = input("Enter your name: ")

        # Display the entered name
        print("Hello,", name)
        print("Welcome to Python Tutorial!")

        # Display the quiz for Lesson 4
        print("\nQUIZ")
        print("Which function accepts user input?")
        print("A. print()")
        print("B. input()")
        print("C. break")

        # Get the student's answer
        answer = input("Your answer: ").upper()

        # Check if the answer is correct
        if answer == "B":
            print("Correct!")
        else:
            print("Incorrect! The answer is B.")

    # ==========================================
    # LESSON 5: CONDITIONAL STATEMENTS
    # ==========================================

    # Check if the student chooses Lesson 5
    elif choice == "5":

        # Display Lesson 5
        print("\nLESSON 5: CONDITIONAL STATEMENTS")

        # Explain conditional statements
        print("\nConditional statements are used to make decisions.")
        print("They use if, elif, and else.")

        # Show an example of conditional statements
        print("\nExample:")
        print("score = 85")
        print("if score >= 75:")
        print('    print("Passed")')
        print("else:")
        print('    print("Failed")')

        # Demonstrate conditional statements
        print("\nTRY IT YOURSELF")

        score = int(input("Enter your score: "))

        # Check if the score is passing or failing
        if score >= 75:
            print("Congratulations! You Passed!")
        else:
            print("Sorry, You Failed.")

        # Display the quiz for Lesson 5
        print("\nQUIZ")
        print("Which statement checks a condition?")
        print("A. if")
        print("B. print")
        print("C. input")

        # Get the student's answer
        answer = input("Your answer: ").upper()

        # Check if the answer is correct
        if answer == "A":
            print("Correct!")
        else:
            print("Incorrect! The answer is A.")

    # ==========================================
    # LESSON 6: LOGICAL OPERATORS
    # ==========================================

    # Check if the student chooses Lesson 6
    elif choice == "6":

        # Display Lesson 6
        print("\nLESSON 6: LOGICAL OPERATORS")

        # Explain logical operators
        print("\nLogical operators are used to combine conditions.")

        print("\nAND - Both conditions must be True.")
        print("OR - At least one condition must be True.")
        print("NOT - Reverses the condition.")

        # Show an example of logical operators
        print("\nExample:")
        print("age = 18")
        print("print(age >= 18 and age <= 60)")
        print("Output: True")

        # Demonstrate the AND operator
        print("\nTRY IT YOURSELF")

        age = int(input("Enter your age: "))

        if age >= 18 and age <= 60:
            print("You are within the age range.")
        else:
            print("You are outside the age range.")

        # Display the quiz for Lesson 6
        print("\nQUIZ")
        print("Which operator requires both conditions to be True?")
        print("A. OR")
        print("B. AND")
        print("C. NOT")

        # Get the student's answer
        answer = input("Your answer: ").upper()

        # Check if the answer is correct
        if answer == "B":
            print("Correct!")
        else:
            print("Incorrect! The answer is B.")

    # ==========================================
    # LESSON 7: ITERATION AND LOOPS
    # ==========================================

    # Check if the student chooses Lesson 7
    elif choice == "7":

        # Display Lesson 7
        print("\nLESSON 7: ITERATION AND LOOPS")

        # Explain iteration and loops
        print("\nIteration means repeating instructions.")
        print("Loops allow a program to repeat tasks.")

        # Introduce the two types of loops
        print("\nThere are two types of loops:")
        print("1. FOR LOOP")
        print("2. WHILE LOOP")

        # Demonstrate the for loop
        print("\nFOR LOOP EXAMPLE")

        for number in range(1, 6):
            print(number)

        # Demonstrate the while loop
        print("\nWHILE LOOP EXAMPLE")

        count = 1

        while count <= 5:
            print(count)
            count += 1

        # Display the quiz for Lesson 7
        print("\nQUIZ")
        print("Which loop repeats while a condition is True?")
        print("A. for")
        print("B. while")
        print("C. if")

        # Get the student's answer
        answer = input("Your answer: ").upper()

        # Check if the answer is correct
        if answer == "B":
            print("Correct!")
        else:
            print("Incorrect! The answer is B.")

    # ==========================================
    # EXIT THE PROGRAM
    # ==========================================

    # Check if the student chooses Exit
    elif choice == "8":

        # Display the goodbye message with the student's name
        print("\nThank you for using Python Tutorial!")
        print("Goodbye,", student_name)

        # Stop the while loop and end the program
        break

    # ==========================================
    # INVALID CHOICE
    # ==========================================

    # Execute this section if the student enters an invalid choice
    else:
        print("\nInvalid choice! Please choose 1 to 8.")

    