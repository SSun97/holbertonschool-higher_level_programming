#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        if div:
            print("Inside result: {}".format(div))
            return div
        else:
            print("Inside result: None")
            return None
