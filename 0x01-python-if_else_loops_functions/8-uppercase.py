#!/usr/bin/env python3
def uppercase(str):
    out = ''
    for n in str:
        if n not in 'abcdefghijklmnopqrstuvwxyz':
            out = out + n
        else:
            k = ord(n)
            l = k - 32
            out = out + chr(1)
    print("{}\n".format(out))
