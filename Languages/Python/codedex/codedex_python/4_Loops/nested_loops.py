# nested loops practice


# for every number in i eg 1, you multiply with j's 1 and 2. so out put will be -> 1,2. and then 2,4. and then 3,6
for i in range(1,4):
        for j in range(1,3):
            print(i * j)


# Nested while loops
i = 0

while i < 3:
    j = 0
    while j < 3:
        print(f"the multiplication is {i} * {j}")
        j = j + 1
        print(f"the j number is {j}")
    i = i + 1
    print(f"the i number is {i}")

# Lucky number generator

import random

lucky_number = random.randint(1,5)
not_found = True

while not_found:
    for i in range(1,6)
        if i == lucky_number:
            not_found = False
            break
        else:
            print(i)
           

print(f"My lucky number is {i}")