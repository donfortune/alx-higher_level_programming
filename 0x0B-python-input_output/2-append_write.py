#!/usr/bin/python3

def append_write(filename="", text=""):
    if not filename:
        print("Your file doesnt exist")

    with open(filename, 'a', encoding='utf-8') as file:
        content = file.write(text)
        num_char = len(str(content))
        print(num_char)
