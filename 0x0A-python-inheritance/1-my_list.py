#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        sort = sorted(self)
        print(sort)
