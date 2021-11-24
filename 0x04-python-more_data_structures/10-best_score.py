#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        max_key = None
    else:
        m = max(a_dictionary.values())
        max_key = (list(a_dictionary.keys())
                   [list(a_dictionary.values()).index(m)])
    return(max_key)
