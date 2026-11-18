#LESSON - Variables Exercise 7
# -----------------------------------------------------

# To check whether a pH level is basic, acidic or neutral

while True:
    try:
        pHLevel = int(input("Please state pH level: "))
        break
    except ValueError:
        print("That is not a valid number. Please Try again: ")

if pHLevel >= 15:
    print("That value is not part of any pH level.")

elif pHLevel > 7:
    print("That is Basic!")

elif pHLevel < 7:
    print("That is Acidic!")

else:
    print("That is neutral!")