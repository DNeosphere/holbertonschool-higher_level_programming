#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        a_char = ord(str[i])
        if (a_char >= 97 and a_char <= 122):
            a_char = a_char - 32
        print("{}".format(chr(a_char)), end='')
    print()
