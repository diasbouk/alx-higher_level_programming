#!/usr/bin/python3

def best_score(a_dictionary):
    max = 0
    
    for k, v in a_dictionary.items():
        if v > max:
            key = k
    return key
