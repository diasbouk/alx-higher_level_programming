#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            checker = 0
        else:
            checker = 1
        str1 = chr(ord(str[i]) - 32)
        print("{}".format(str1 if checker == 0 else str[i]), end="")
    print("")
