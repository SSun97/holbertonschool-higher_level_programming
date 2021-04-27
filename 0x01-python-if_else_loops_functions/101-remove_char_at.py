#!/usr/bin/python3
def remove_char_at(str_scr='', n=0):
    str_cp = ''
    for i in range(len(str_scr)):
        if i == n:
            continue
        str_cp = str_cp + str_scr[i]
    return str_cp
