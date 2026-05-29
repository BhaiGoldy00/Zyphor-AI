import time
import random

print("This is Zyphor AI . Your personal AI chatbot made by BhaiGoldy00.")

time.sleep(4)
print()

name = input("Your Good Name : ")

time.sleep(1)
print()

print("Hi , Nice to meet you", name, "!")
print()

time.sleep(1)

agree = input("Would you like to know what stuff I can do ! ")

print()

if agree.lower() == "yes":

    print("Glad to see you wanted to know ")
    time.sleep(2)
    print()

    print("I can help you with basic maths like add, sub, multiply or divide.")
    time.sleep(2)

    print("I can also challenge you for a fun puzzle game and give you scores as per your answers")
    print()

    time.sleep(2)

    print("Note that I'm a very basic chatbot , so you can only choose from what I offer ")
    print()

    time.sleep(2)

    ask = input("So do you wanna play a quiz or want a mathematical help ? : ")

    print()

    # ---------------- QUIZ ---------------- #

    if ask.lower() == "quiz":

        print("All right , get ready for it")
        time.sleep(1)

        score = 0

        print()
        print("Your current score = 0")
        print()

        question1 = input("Which planet is known as Red Planet ? - ")

        if question1.lower() == "mars":
            print()
            print("You're correct , Now next question")
            score += 1
            print("Your score =", score)
            print()

        else:
            print("You are wrong")
            print("Correct answer was Mars")
            print()

        time.sleep(1)

        question2 = input("What's 77 + 33 ? - ")

        if question2 == "110":
            print()
            print("Great !!!!! ")
            score += 1
            print("Your score =", score)
            print()

        else:
            print("You are wrong buddy :( ")
            print("Correct answer was 110")
            print()

        time.sleep(1)

        question3 = input("Who is known as the Father of Computer ? - ")

        if question3.lower() == "charles babbage":
            print()
            print("Amazing answer !")
            score += 1
            print("Your score =", score)
            print()

        else:
            print("Wrong answer")
            print("Correct answer was Charles Babbage")
            print()

        time.sleep(1)

        print("Quiz Finished !!!!!")
        print()

        print("Final Score =", score, "/3")

        if score == 3:
            print("Excellent performance 🔥")

        elif score == 2:
            print("Very Good 😎")

        elif score == 1:
            print("Nice try 🙂")

        else:
            print("Better luck next time 😅")

    # ---------------- MATHS ---------------- #

    elif ask.lower() == "mathematical help":

        print("Nice ! I can do:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print()

        choice = input("Choose your operation : ")

        print()

        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        print()

        if choice.lower() == "addition":
            print("Answer =", num1 + num2)

        elif choice.lower() == "subtraction":
            print("Answer =", num1 - num2)

        elif choice.lower() == "multiplication":
            print("Answer =", num1 * num2)

        elif choice.lower() == "division":

            if num2 == 0:
                print("Division by zero is not possible")

            else:
                print("Answer =", num1 / num2)

        else:
            print("Invalid operation selected")

    else:
        print("Please choose only from quiz or mathematical help")

else:
    print("No worry, say to me freely whenever you need my help")
