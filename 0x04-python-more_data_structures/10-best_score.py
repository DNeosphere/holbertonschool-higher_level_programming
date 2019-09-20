#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxim = max(zip(a_dictionary.values(), a_dictionary.keys()))
    if maxim is None:
        return None
    return maxim[1]
