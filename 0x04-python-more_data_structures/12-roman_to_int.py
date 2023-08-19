#!/usr/bin/python3
# Lujaja Luvuga

def roman_to_int(roman_string):
    """converts a roman numeral to an integer"""
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    r_dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    decimal = 0

    for l in range(len(roman_string)):
        if r_dictionary.get(roman_string[l], 0) == 0:
            return (0)

        if l != (len(roman_string[l]) - 1) and r_dictionary[roman_string[l]] < \
                r_dictionary[roman_string[l + 1]]:
                    decimal += r_dictionary[roman_string[l]] * -1
        else:
            decimal += r_dictionary[roman_string[l]]

    return (decimal)
