#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as cal
    import sys
    argv = sys.argv
    length = len(argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if operator == '+':
        print(f"{a} {operator} {b} = {cal.add(a, b)}")
    elif operator == '-':
        print(f"{a} {operator} {b} = {cal.sub(a, b)}")
    elif operator == '*':
        print(f"{a} {operator} {b} = {cal.mul(a, b)}")
    elif operator == '/':
        print(f"{a} {operator} {b} = {cal.div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
