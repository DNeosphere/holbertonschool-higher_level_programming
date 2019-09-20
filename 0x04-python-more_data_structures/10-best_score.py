#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    maxim = max(zip(a_dictionary.values(), a_dictionary.keys()))
    if maxim is 0:
        return None
    return maxim[1]
