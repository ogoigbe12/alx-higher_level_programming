#!/usr/bin/python3
for s in range(0, 9):
    for d in range(s + 1, 10):
        if s == 8:
            print("{}{}".format(s,d))
        else:
            print("{}{}".format(s,d),end=", ")
