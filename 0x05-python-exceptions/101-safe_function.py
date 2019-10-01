#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        total = fct(*args)
    except Exception as msg:
        total = None
        print("Exception: {}".format(str(msg)), file=sys.stderr)
    return total
