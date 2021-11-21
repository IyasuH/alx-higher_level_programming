#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if (n == 0):
        return(None)
    else:
        high = my_list[0]
        for i in my_list:
            if (i > high):
                high = i
        return(high)
