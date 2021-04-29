#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 and set_2:
        return {item for item in set_1 if item not in set_2}\
                | {item for item in set_2 if item not in set_1}
    elif set_1 == set_2 and set_2 == {}:
        return {}
    elif set_1 == {}:
        return set_2
    elif set_2 == {}:
        return set_1
