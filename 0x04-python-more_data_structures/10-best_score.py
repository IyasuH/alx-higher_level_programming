#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        max_key = None
    else:
        max_key = max(a_dictionary.values())
    return(max_key)
