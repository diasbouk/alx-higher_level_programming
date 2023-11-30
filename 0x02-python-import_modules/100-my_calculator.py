#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+':
        result = add(int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))

    elif argv[2] == '-':
        result = sub(int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format((argv[1], argv[2], argv[3], result)))

    elif argv[2] == '*':
        result = mul(int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))

    elif argv[2] == '/':
        result = div(int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
