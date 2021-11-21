#!/usr/bin/python3
def no_c(my_string):
    list1 = []
    list1[:0] = my_string
    n = len(list1)
    b = list1.count("C")
    s = list1.count("c")
    c = s + b
    t = n - c - 2
    str1 = ""
    for i in range(t):
        if(list1[i] == 'c' or list1[i] == 'C'):
            list1.pop(i)
    for ele in list1:
        str1 += ele
    return (str1)
