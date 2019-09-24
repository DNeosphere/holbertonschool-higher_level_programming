#!/usr/bin/python3
def islower(c):
    ascii_char = ord(c)
    if ascii_char >= 97 and ascii_char <= 122:
        return True
    else:
        return False
