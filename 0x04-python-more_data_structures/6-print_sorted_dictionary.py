#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for u in sorted(a_dictionary):
        print("{:s}: {}".format(u, a_dictionary[u]))
