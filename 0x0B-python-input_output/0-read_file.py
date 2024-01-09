#!/usr/bin/python3

def read_file(filename="", encoding="utf-8"):
    with open(filename) as file:
        content = file.read()
        print(content)
