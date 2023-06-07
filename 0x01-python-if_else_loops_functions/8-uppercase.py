#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            upper_char = chr(ord(c) - ord('a') + ord('A'))
            result += "{}".format(upper_char)
        else:
            result += "{}".format(c)
    print(result)
