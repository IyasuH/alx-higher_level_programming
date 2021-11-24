#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    d = {key: value}
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        a_dictionary.update(d)
    return(a_dictionary)
