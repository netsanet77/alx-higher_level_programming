#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    length = len(argv) - 1
    result = 0
    for i in range(1, length + 1):
        result = result + int(argv[i])
    print(f"{result}")
