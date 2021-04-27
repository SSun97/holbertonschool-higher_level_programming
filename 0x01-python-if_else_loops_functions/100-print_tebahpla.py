#!/usr/bin/python3
for i, j in zip(range(ord('a'), ord('z') + 1), range(0, 26)):
    print("{}".format(chr(ord('a') + 25 - j) if j % 2 == 0
          else chr(ord('a') + 25 - j - 32)), end='')
