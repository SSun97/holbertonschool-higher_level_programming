#!/usr/bin/python3
import sys
if __name__ == '__main__':
    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    else:
        print("{} argument{}".format(len(sys.argv) - 1,
              ":" if len(sys.argv) == 2 else "s:"))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
