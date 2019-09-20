#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    dic_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    len_string = len(roman_string)
    res = dic_num[roman_string[len_string-1]]

    for i in range(len_string-1, 0, -1):
        current = dic_num[roman_string[i]]
        prev = dic_num[roman_string[i-1]]
        if prev >= current:
            res += prev
        else:
            res -= prev
    return res
