#LESSON - Variables Exercise 7
# -----------------------------------------------------

# To check whether a pH level is basic, acidic or neutral


while True:
    try:
        pHLevel = int(input("Please state pH level: "))
        break
    except ValueError:
        print("Invalid pH level, please try again: ")