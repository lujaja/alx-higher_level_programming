#!/usr/bin/python3
import random
number = random.randint(-1000, 10000)
print(f"Last digit of {number} is", end=' ')

if number < 0:
    number = -number
    print(f"{number % 10}", end=' ')
else:
    print(f"{number % 10}", end=' ')
if (number % 10) > 5:
    print(f"and if greater than 5")
elif (number % 10) < 6 and not 0:
    print(f"and is less than 6 and not 0")
else:
    print(f"and is 0")
