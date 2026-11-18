#LESSON - Variables Exercise 11
# -----------------------------------------------------

# TASK: to see a demo using a bank's ATM.


print('BANK OF CODÉDEX')

# Requests user to input Bank PIN number
pin = int(input('Enter your PIN: '))

# While the result of pin is not 1234, Request user to enter PIN again.
while pin != 1234:
    pin = int(input('Incorrect PIN. Enter your PIN again: '))

# If pin is 1234, break while loop and tell user that PIN is accepted.
if pin == 1234:
    print('PIN accepted!')