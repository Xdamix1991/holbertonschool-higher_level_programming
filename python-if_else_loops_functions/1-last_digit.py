#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#extracting last degit
last_digit_number = number % 10

#ajust extracted number if number is negative
if number < 0 and last_digit_number != 0:
    last_digit_number -= 10

if last_digit_number > 5:
    print("Last digit of {} is {} and is greater than 5". format(number, last_digit_number))

if last_digit_number == 0:
    print("Last digit of {} is {} and is 0". format(number, last_digit_number))

if last_digit_number < 6:
    print("Last digit of {} is {} and is less than 6 and not 0". format(number, last_digit_number))

