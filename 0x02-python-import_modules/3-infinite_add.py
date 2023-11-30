#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = 0
    if len(sys.argv) - 1 == 0:
        print("{}".format(0))
    else:
        for j in range(1, len(sys.argv)):
            count += int(sys.argv[j])
        print("{}".format(count))
