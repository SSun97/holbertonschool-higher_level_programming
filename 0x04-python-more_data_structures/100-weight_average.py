#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        list_score = []
        list_weight = []
        sumn = 0
        div = 0
        for i in range(len(my_list)):
            sumn += my_list[i][0] * my_list[i][1]
            div += my_list[i][1]
        return sumn / div
    else:
        return 0
