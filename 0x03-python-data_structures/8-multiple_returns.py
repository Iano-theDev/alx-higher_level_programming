#!/usr/bin/python3
def multiple_returns(sentence):
    a = (0, None) if not sentence else (len(sentence), sentence[0])
    return a
