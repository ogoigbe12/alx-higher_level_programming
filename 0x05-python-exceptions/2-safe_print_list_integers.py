#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for v in range(o, x):
        try:
            print("{:d}".format(my_list[v]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
        print()
        return count
