#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_files = list(map(lambda x: replace if x == search else x, my_list))
    return (replaced_files)

