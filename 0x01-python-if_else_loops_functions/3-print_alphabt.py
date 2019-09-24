#!/usr/bin/python3
for alpha in range(97, 123):
    if alpha == 101 or alpha == 113:
        continue
    print("{}".format(chr(alpha)), end='')
