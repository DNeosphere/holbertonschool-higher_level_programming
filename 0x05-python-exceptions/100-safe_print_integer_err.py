#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as ex_err:
        print("Exception: {}".format(str(ex_err)), file=sys.stderr)
        return False
    return True
