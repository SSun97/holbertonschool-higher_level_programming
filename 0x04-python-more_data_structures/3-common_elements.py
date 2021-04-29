#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        return {item for item in set_1 if item in set_2}
    else:
        return {}
