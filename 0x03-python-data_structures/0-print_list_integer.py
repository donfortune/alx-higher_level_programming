#!/usr/bin/python3

def print_list_integer(my_list=None):
    if my_list is None:
        my_list = []
    for item in my_list:
        print(item)

print_list_integer([1, 2, 3, 4, 5])

