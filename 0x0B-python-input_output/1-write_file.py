#!/usr/bin/python3

def write_file(filename="", text=""):
    if not filename:
        print('file created succesfully')
    with open(filename, 'w', encoding="utf-8") as file:
            content = file.write(text)
            num_char = len(str(content))
            print(num_char)
