#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000}
    if not isinstance(roman_string, str):
        return 0
    result = 0
    length = len(roman_string)

    for i in range(length):
        value = roman_numbers[roman_string[i]]

        if i + 1 < length and value < roman_numbers[roman_string[i + 1]]:
            result -= value
        else:
            result += value

    return result
