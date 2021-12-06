#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = [None] * list_length
    for i in range(list_length):
        try:
            div[i] = my_list_1[i]/my_list_2[i]
        except (ZeroDivisionError):
            print("division by 0")
            div[i] = 0
        except(TypeError, ValueError):
            print("wrong type")
            div[i] = 0
        except(IndexError):
            print("out of range")
            div[i] = 0
    return (div)
