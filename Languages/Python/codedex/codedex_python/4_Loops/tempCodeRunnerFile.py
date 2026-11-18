import random

lucky_number = random.randint(1,5)
not_found = True

while not_found:
    for i in range(1,5):
        if i == lucky_number:
            not_found = False
            break
        else:
            print(i)
           

print(f"My lucky number is {i}")