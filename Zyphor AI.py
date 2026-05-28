import time
print("This is Zyphor AI . Your personal AI chatbot made by BhaiGoldy00.")

time.sleep(4)
print()

name = input("Your Good Name : ")

time.sleep(1)
print()

print("Hi , Nice to meet you" ,name, "!")
print()
time.sleep(1)
agree = input("Would you like to know what stuff I can do ! ")

print()
time.sleep(0)

if agree.lower() == "yes":
    print("Good to see you wanted to know ")
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
    ask = input("So do you wanna play a quiz or want a mathematical help ? :")
    
    if ask.lower() == "quiz":
        print("All right , get ready for it")
        time.sleep(1)
        print()
        print("Your current score = 0")
        
        time.sleep(0)
        print()

        question1 = input("Which planet is known as Red Earth - ")
        if question1.lower() == "mars":
            print()
            print("Your're correct , Now next question")
            print()
        else:
            print("You are wrong") 
          
            time.sleep(1)
            
        question2 = input("What's 77+33 ? - ")
        if question2 == "110":
            print()
            print("Great !!!!! ")
            
        else:
            print("You are wrong buddy :( ")
           
else:
    print("No worry, say to me freely whenever you need my help")
    

