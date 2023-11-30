#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    if len(sys.argv) - 1 == 0:
        print("{} arguments.".format(0))
    elif len(sys.argv) - 1 == 1:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
