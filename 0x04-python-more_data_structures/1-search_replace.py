#!/usr/bin/python3
def search_replace(my_list, search, replace):
    idx = my_list.index(search)
    new = my_list.copy()
    new[idx] = replace
    return(new)
