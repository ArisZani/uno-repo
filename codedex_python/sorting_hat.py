#LESSON - Variables Exercise 10
# -----------------------------------------------------

# TASK: To write a program that asks the user some questions with the int() and input() functions


# h1_name = "Gryffindor"
# h1_score = 0

# h2_name = "Ravenclaw"
# h2_score = 0

# h3_name = "Hufflepuff"
# h3_score = 0

# h4_name = "Slytherin"
# h4_score = 0

# while True:
#     try:
#         userHouse = int(input("Please state your house:\n1) Gryffindor\n2) Ravenclaw\n3) Hufflepuff\n4) Slytherin\nAnswer: "))

#         if userHouse == 1:
#             print("You chose Gryffindor!")
            
#         elif userHouse == 2:
#             print("You chose Ravenclaw!")
           
#         elif userHouse == 3:
#             print("You chose Hufflepuff!")
          
#         elif userHouse == 4:
#             print("You chose Slytherin!")
          
#         else:
#             print("Invalid House")
#             break

#     except ValueError:
#         print("That is not a number. Please try again.")

#     while True:
#             try:
#                 questionOne = input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\nAnswer: ")
#                 qnone = int(questionOne)

#                 if qnone == 1:
#                     h1_score += 1
#                     h2_score += 1
#                     print(f"{h1_name} and {h2_name} now have {h1_score} and {h2_score} respectively!")
#                     break

#                 elif qnone == 2:
#                     h2_score += 1
#                     h4_score += 1
#                     print(f"{h3_name} and {h4_name} now have {h3_score} and {h4_score} respectively!")
#                     break

#                 else:
#                     print("Wrong input")
#                     break


#             except ValueError:
#                 print("Invalid input, please use numbers only.")

#     while True:
#                 try:
#                     questionTwo = input("Q1) When I'm dead, I want people to remember me as\n1) The good\n2) The great\n3) The wise\n4) The Bold\nAnswer: ")
#                     qntwo = int(questionTwo)

#                     if qntwo == 1:
#                         h3_score += 1
#                         print(f"{h3_name} has {h3_score} points now!")
#                         continue

#                     if qntwo == 2:
#                         h4_score += 1
#                         print(f"{h4_name} has {h4_score} points now!")
#                         continue

#                     if qntwo == 3:
#                         h2_score += 1
#                         print(f"{h2_name} has {h2_score} points now!")
#                         continue

#                     if qntwo == 4:
#                         h1_score += 1
#                         print(f"{h1_name} has {h1_score} points now!")
#                         continue

                
                #     else:
                #         print("Wrong input")
                #         break

                # except ValueError:
                #     print("Invalid input, please use numbers only.")






#LESSON - Variables Exercise 10
# -----------------------------------------------------

h1_name = "Gryffindor"
h1_score = 0

h2_name = "Ravenclaw"
h2_score = 0

h3_name = "Hufflepuff"
h3_score = 0

h4_name = "Slytherin"
h4_score = 0

# --- STEP 1: CHOOSE A HOUSE ---
while True:
    try:
        userHouse = int(input("Please state your house:\n1) Gryffindor\n2) Ravenclaw\n3) Hufflepuff\n4) Slytherin\nAnswer: "))

        if userHouse == 1:
            userHouse = 'Gryffindor'
            print("You chose Gryffindor!")
            break # Valid choice! Exit loop and move to questions
        elif userHouse == 2:
            userHouse = 'Ravenclaw'
            print("You chose Ravenclaw!")
            break
        elif userHouse == 3:
            userHouse = 'Hufflepuff'
            print("You chose Hufflepuff!")
            break
        elif userHouse == 4:
            userHouse = 'Slytherin'
            print("You chose Slytherin!")
            break
        else:
            print("Invalid House. Please select 1-4.")
            # Keep looping until they pick a valid house

    except ValueError:
        print("That is not a number. Please try again.")

# --- STEP 2: QUESTION ONE ---
while True:
    try:
        questionOne = input("\nQ1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\nAnswer: ")
        qnone = int(questionOne)

        if qnone == 1:
            h1_score += 1
            h2_score += 1
            print(f"{h1_name} and {h2_name} now have {h1_score} and {h2_score} respectively!")
            break # Move to next question

        elif qnone == 2:
            h2_score += 1
            h4_score += 1
            # Corrected text to show Ravenclaw and Slytherin to match the math above
            print(f"{h2_name} and {h4_name} now have {h2_score} and {h4_score} respectively!")
            break # Move to next question

        else:
            print("Wrong input. Please choose 1 or 2.")

    except ValueError:
        print("Invalid input, please use numbers only.")

# --- STEP 3: QUESTION TWO ---
while True:
    try:
        questionTwo = input("\nQ2) When I'm dead, I want people to remember me as\n1) The good\n2) The great\n3) The wise\n4) The Bold\nAnswer: ")
        qntwo = int(questionTwo)

        if qntwo == 1:
            h3_score += 1
            print(f"{h3_name} has {h3_score} points now!")
            break # CHANGED from continue to break out of the loop cleanly

        elif qntwo == 2:
            h4_score += 1
            print(f"{h4_name} has {h4_score} points now!")
            break

        elif qntwo == 3:
            h2_score += 1
            print(f"{h2_name} has {h2_score} points now!")
            break

        elif qntwo == 4:
            h1_score += 1
            print(f"{h1_name} has {h1_score} points now!")
            break

        else:
            print("Wrong input. Please choose 1-4.")

    except ValueError:
        print("Invalid input, please use numbers only.")

# --- STEP 4: QUESTION THREE ---
while True:
    try:
        questionThree = input("\nQ2) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\nAnswer: ")
        qnthree = int(questionThree)

        if qnthree == 1:
            h4_score += 4
            print(f"{h4_name} has {h4_score} points now!")
            break # CHANGED from continue to break out of the loop cleanly

        elif qnthree == 2:
            h3_score += 4
            print(f"{h3_name} has {h3_score} points now!")
            break

        elif qnthree == 3:
            h2_score += 4
            print(f"{h2_name} has {h2_score} points now!")
            break

        elif qnthree == 4:
            h1_score += 4
            print(f"{h1_name} has {h1_score} points now!")
            break

        else:
            print("Wrong input. Please choose 1-4.")

    except ValueError:
        print("Invalid input, please use numbers only.")



# --- FINAL SCOREBOARD ---
print("\n--- FINAL HOUSE SCORES ---")
print(f"{h1_name}: {h1_score}")
print(f"{h2_name}: {h2_score}")
print(f"{h3_name}: {h3_score}")
print(f"{h4_name}: {h4_score}\n")

if userHouse == 'Gryffindor':
    print(f"{h1_name} has a total of {h1_score} points!")

elif userHouse == 'Ravenclaw':
    print(f"{h2_name} has a total of {h2_score} points!")

elif userHouse == 'Hufflepuff':
    print(f"{h3_name} has a total of {h3_score} points!")

elif userHouse == 'Slytherin':
    print(f"{h4_name} has a total of {h4_score} points!")