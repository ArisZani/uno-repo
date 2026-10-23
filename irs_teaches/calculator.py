#Calculator with 4 Functions

# + --> +
# - --> -
# x --> *
# / ---> /
# ^2 ---> ** 2

# toAdd(a: int, b: int) -> int
# toSubtract(a: int, b: int) -> int
# toMultiply(a: int, b: int) -> int
# toDivide(a: int, b: int) -> int

#constants
LANGUAGE = "Java"

print(f"{LANGUAGE}")

# Defining toAdd
def toAdd(a,b):
    """
    This method takes in two integers a and b.
    It then returns the sum of those integers.
    """
    return a + b 


def toAddv2(a,b):
    """
    This method takes in two integers a and b.
    It then returns the sum of those integers.
    """
    c = a + b
    return c

# Abstracted
# print(toAdd(6, 8))
# print(6 + 8)

# print(toAddv2(6, 8))
# print(14)

# Defining toSubtract
