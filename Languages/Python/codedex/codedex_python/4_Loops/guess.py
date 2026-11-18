#LESSON - Variables Exercise 12
# -----------------------------------------------------

# TASK: to create a guessing game but there is a new limit to the number of tries (not infinite)

tries = 5
guess = 0

while guess != 6:
    guess = int(input("Guess the number: "))
    if guess == 6:
        break
    if guess != 6: 
        tries -= 1
    print(f"You have {tries} left.")
    if tries == 0:
        print("You have no more tries. See you next time!")
        break

if guess == 6:
    print("You got it!")



# From AI Coding Companion, CLEANER

tries = 5

while tries > 0:
    guess = int(input("Guess the number: "))

    if guess == 6:
        print("You got it!")
        break

    tries -= 1

    if tries == 0:
        print("You have no more tries. See you next time!")
    else:
        print(f"You have {tries} left.")