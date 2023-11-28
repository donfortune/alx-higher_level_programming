#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = number % 10
if new_number > 5:
    print(f"Last digit of {number} is {new_number} and is greater than 5")
if new_number == 0:
    print(f"Last digit of {number} is {number} and is 0")
if 0 < new_number < 6 and new_number != 0:
    print(f"Last digit of {number} is {new_number}, less than 6 and not 0")
