#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def arg_count(argc, argv):
        if argc == 1:
            print('1 argument:')
            print(f"1: {argv[0]}")
        elif argc > 1:
            print(f"{argc} arguments:")
            for i, arg in enumerate(argv, 1):
                print(f"{i}: {arg}")
        else:
            print("No arguments provided.")

argc = len(sys.argv) - 1
argv = sys.argv[1:]
arg_count(argc, argv)

