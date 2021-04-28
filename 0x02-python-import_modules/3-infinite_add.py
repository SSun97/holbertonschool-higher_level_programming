#!/usr/bin/python3
import sys
if __name__ == '__main__':
    summ = 0
    n = len(sys.argv)
    if n == 1:
        print("0")
    else:
        for i in range(1, n):
            summ = summ + int(sys.argv[i])
        print(summ)
