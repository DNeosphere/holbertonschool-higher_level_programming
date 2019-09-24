#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv)

    if len_argv == 1:
        print("0 arguments.")
        exit()
    elif len_argv == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len_argv - 1))

        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
