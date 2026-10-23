#LESSON - Variables Exercise 5
# -----------------------------------------------------

# TASK: Create a program that asks the user for the amount they have in pesos, soles, and reais
# and calculates the total in USD

# Enquire user the amount in pesos
while True:
    try:
        pesos = float(input("How much do you have in pesos? ANS: "))
        break
    except ValueError:
        print("Invalid Input. Please try again!")

# Enquire user the amount in soles
while True:
    try:
        soles = float(input("How much do you have in soles? ANS: "))
        break
    except ValueError:
         print("Invalid Input. Please try again!")

# Enquire user the amount in reais
while True:
    try:
        reais = float(input("How much do you have in reais? ANS: "))
        break
    except ValueError:
         print("Invalid Input. Please try again!")


# Conversion rate for USD to Colombian pesos: 1 = 0.00032
# Conversaion rate for USD to Peruvian soles: 1 = 0.29
# Conversaion rate for USD to Brazilizan reais: 1 = 0.20

totalLeft = (pesos * 0.0032 + soles * 0.29 + reais * 0.20)
print("Total amount left (in USD): ", totalLeft)