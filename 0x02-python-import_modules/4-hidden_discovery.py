#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    all_variables = dir(hidden_4)
    for name in all_variables:
        if not name.startswith('__'):
            print(name)
