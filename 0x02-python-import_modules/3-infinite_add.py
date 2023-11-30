#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def infinite_add(argv):
        numbers = [int(arg) for arg in argv]
        total = sum(numbers)
        print(total)


    argv = sys.argv[1:]
    infinite_add(argv)
