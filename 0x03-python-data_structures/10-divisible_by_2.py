#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = len(my_list)
    new_list = my_list.copy()
    for i in range(0, n):
        if(my_list[i] % 2 == 0):
            new_list[i] = True
        else:
            new_list[i] = False
    return(new_list)
