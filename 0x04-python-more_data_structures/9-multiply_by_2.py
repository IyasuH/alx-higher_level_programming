#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in a_dictionary:
        new_dict[i] = a_dictionary[i]
    new_dict.update((x, y*2) for x, y in new_dict.items())
    return(new_dict)
