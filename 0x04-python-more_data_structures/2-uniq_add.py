#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        summ = 0
        uniq_list = list(set(my_list))
        for x in uniq_list:
            summ += x
        return summ
    else:
        return 0
