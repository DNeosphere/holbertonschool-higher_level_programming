#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    if len_sentence is None:
        char = None
    else:
        char = sentence[0]
    return len_sentence, char
