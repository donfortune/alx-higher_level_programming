#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    for i, j in a_dictionary.items():
        print(len(i))
        num += 1

    return num
