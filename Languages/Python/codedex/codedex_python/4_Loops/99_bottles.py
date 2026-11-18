#LESSON - Variables Exercise 14
# -----------------------------------------------------

# TASK: To use For loop and a range() function to print out all the verses of 99 bottles of Beer.

b_no = 99


for i in range(99):
    word = "bottles" if b_no != 1 else "bottle" 
    print(f"{b_no} {word} of beer on the wall!")
    print(f"{b_no} {word} of beer!")
    print("Take one down, pass it around.")
    b_no -= 1

    if b_no == 1:
        print(f"{b_no} bottle of beer on the wall!")
    else:
        print(f"{b_no} bottles of beer on the wall!")



#
    #if b_no == 1:
       #print(f"{b_no} bottle of beer on the wall!")
        #print(f"{b_no} bottle of beer!")
        #print("Take one down, pass it around.")
        #b_no -= 1
        #print(f"{b_no} bottles of beer on the wall!")
    #if b_no == 0:
    