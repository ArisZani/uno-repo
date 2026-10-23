#LESSON - Variables Exercise 4
# -----------------------------------------------------

# TASK: Create a program that asks the user for two numbers, 'a' and 'b' and then
# calculates the hypotenuse 'c'.

# Pythagoras theorem = c ** 2 = (a ** 2 + b ** 2) ** 0.5

a = int(input('Please input length of Side a: '))
b = int(input('Please input length of Side b: '))
Hypotenuse = (a ** 2 + b ** 2) ** 0.5 
print('The Hypotenuse is:', Hypotenuse)
