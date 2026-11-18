#LESSON - Variables Exercise 8
# -----------------------------------------------------

# A program that can respond to any Yes or NO questions with a different answer each time it executes

import random

Question = input("Ask your close-ended question here: ")

num = random.randint(1,9)

if num == 1:
    print("Yes - definitely")

elif num == 2:
    print("It is decidedly so")

elif num == 3:
    print("Yep yepp")

elif num == 4:
    print("OF COURSE!")

elif num == 5:
    print("FOR SURE.")

elif num == 6:
    print("Nope.")

elif num == 7:
    print("No!")

elif num == 8:
    print("Preferably not.")

elif num == 9:
    print("I do not think so.")

else:
    print("huh")

# Second option -> putting replies as part of a list

import random

answers = [
    "Yes",
    "No",
    "Right",
    "Maybe not"
]

while True: 
    YNQUestion = input("What is your question: ")
    selected_answer = random.choice(answers)
    print("My answer for you is: ", selected_answer)