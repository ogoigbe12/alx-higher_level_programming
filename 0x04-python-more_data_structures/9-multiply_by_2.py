#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for o in a_dictionary:
        new_d[o] = a_dictionary[o] * 2
        return new_d

