#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max_score = 0
    for key, score in a_dictionary.items():
        if score > max_score:
            max_score = score
            max_key = key
    return max_key
