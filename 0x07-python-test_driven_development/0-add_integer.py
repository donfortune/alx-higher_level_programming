def add_integer(a, b=98):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("a and b must be integers or floats")

    new_num = int(a)
    new_num2 = int(b)

    if new_num != a or new_num2 != b:
        raise TypeError("a must be an integer or b must be an integer")

    return new_num + new_num2
