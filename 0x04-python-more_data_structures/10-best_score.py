#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        m = max(a_dictionary.values())
        max_key = (list(a_dictionary.keys())
                   [list(a_dictionary.values()).index(m)])
    else:
        max_key = None
    return(max_key)
