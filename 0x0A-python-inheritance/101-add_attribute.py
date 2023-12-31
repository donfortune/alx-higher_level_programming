#!/usr/bin/python3

def add_func(obj, attr, value):
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__') and '__dict__' in type(obj).__slots__):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

