#LESSON - Variables Exercise 9
# -----------------------------------------------------

# Asks the user what their height iss and how many credits they hae and store the values in a height variable and credits variable

# "while True" used to dictate a while loop
while True:
    try:
        height = (input("Please enter your height(in meters): "))
        # Assigns a variable "num_h" to height while indicating data type
        num_h = float(height)

        if num_h < 1.37 :
            print("You are not tall enough! You cannot join the ride.")
            # Uses "continue" to get out of loop to go on with code
            continue

        elif num_h >= 1.37 :
            # Uses an "f" before quotation to tell to find value of the variable in {}
            print(f"Result: {num_h} is valid.")
             
            # An indented "while True" to show that it is connected with the first while loop
            while True:
                    try:
                        credits = (input("Please enter how many credits you have: "))
                        num_c = int(credits)

                        if num_c < 10:
                            print("You do not have enough credits! Resetting you back to height selection.")
                            # Uses "break" to end loop here and go back to first while loop
                            break

                        elif num_c >= 10:
                            print(f"Result: {num_c} credits. You have enough to hop on the ride!")
                            
                        if num_h >= 1.37 and num_c >= 10:
                            print(f"You are {num_h} meters tall and you have {num_c} credits. Enjoy the ride!")
                            exit()

                    # an exception for nested loop        
                    except ValueError:
                            print("That is not a number. Please try again.")

    # an exception for outermost loop
    except ValueError:
        print("That is not a number. Please try again.")
    
  