#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
        eles:
            for r in a_dictionary:
                if r == key:
                    a_dictionary[r] = value
                    return a_dictionary
