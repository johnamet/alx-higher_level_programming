#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, type("")):
        return 0

    roman_string = roman_string.upper()

    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    _sum = 0

    for i in range(len(roman_string)):
        value = nums[roman_string[i]]

        if i+1 < len(roman_string) and nums[roman_string[i+1]] > value:
            _sum -= value
        else:
            _sum += value

    return _sum
