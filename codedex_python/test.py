while True:  # --- FIRST LOOP (HEIGHT) ---
    try:
        height = input("Please enter your height(in meters): ")
        num_h = float(height)

        if num_h < 1.37:
            print("You are not tall enough! You cannot join the ride.")
            continue
        elif num_h >= 1.37:
            print(f"Result: {num_h} is valid.")
            
            # --- SECOND LOOP (CREDITS) IS NOW NESTED INSIDE ---
            # This only triggers if they pass the height requirement
            while True: 
                try:
                    credits = input("Please enter how many credits you have: ")
                    num_c = int(credits)
                    
                    if num_c < 10:
                        print("You do not have enough credits! Resetting back to the height selection.")
                        break  # <--- THIS exits the credit loop, which automatically restarts the height loop!
                        
                    elif num_c >= 10:
                        print(f"Result: {num_c} credits. You have enough to hop on the ride!")
                        
                        # --- FINAL SUCCESS MESSAGE ---
                        print(f"You are {num_h} meters tall and you have {num_c} credits. Enjoy the ride!")
                        exit()  # Stops the entire program cleanly since they passed everything!
                        
                except ValueError:
                    print("That is not a number. Please try again.")
             
    except ValueError:
        print("That is not a number. Please try again.")
