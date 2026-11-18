#LESSON - Variables Exercise 27 (numbering following Codedex)
# -----------------------------------------------------

# TASK: To use functions

User_age = int(input("How old are you? \nYour response:"))
print(f"You are {User_age} years old!")

chicken = [0.2, 0.1, 0.3]
for i in range(len(chicken)):
    print("Hi!")
    for j in chicken:
        j = -2
        print("Hello!")

fruits = "Apple", "Banana", "Mango"
print(reversed(fruits))