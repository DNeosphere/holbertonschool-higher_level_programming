#!/usr/bin/python3
for first_num in range (0, 9):
    for sec_num in range (1, 10):
        if first_num == 8 and sec_num == 9:
            print("{}{}".format(first_num, sec_num))
            break
        if first_num == sec_num:
            continue
        print("{}{}, ".format(first_num, sec_num), end='')
