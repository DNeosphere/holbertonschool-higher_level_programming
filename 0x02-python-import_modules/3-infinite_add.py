#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_var = 0
    for i in range(1, len(argv)):
        sum_var += int(argv[i])
    print("{}".format(sum_var))
