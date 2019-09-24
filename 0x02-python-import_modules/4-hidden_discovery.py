#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidd_str = dir(hidden_4)
    for i in hidd_str:
        if i[0] == "_":
            continue
        print("{}".format(i))
