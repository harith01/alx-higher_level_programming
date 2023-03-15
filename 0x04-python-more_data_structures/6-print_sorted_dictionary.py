#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    index = sorted(a_dictionary)
    for key in index:
        print("{:s}: {}".format(key, a_dictionary[key]))
