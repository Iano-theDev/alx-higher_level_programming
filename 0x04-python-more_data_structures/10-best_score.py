#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_val = max(a_dictionary.values())
        for k, v in a_dictionary.items():
            if v == max_val and k is not None:
                return k
    return None
