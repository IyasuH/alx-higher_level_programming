#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    high = 0
    if (n == 0):
        return(None)
    else:
        for i in my_list:
            if (i > high):
                high = i
        return(high)
