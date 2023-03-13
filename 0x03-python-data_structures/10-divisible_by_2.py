#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple_2 = []
    for n in my_list:
        if n % 2 == 0:
            multiple_2.append(True)
        else:
            multiple_2.append(False)
    return multiple_2
