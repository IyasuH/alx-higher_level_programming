#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new = list(dict.fromkeys(my_list))
    for i in range(len(new)):
        sum = sum + new[i]
    return(sum)
