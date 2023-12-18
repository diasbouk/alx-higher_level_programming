#!/usr/bin/pytohn3
def list_division(my_list1, my_list2, list_length):
    new_list = []
    exceptions = [ZeroDivisionError("division by 0"), IndexError("out of range"), TypeError("wrong type")]
    for i in range(0, list_length):
        try:
            new_list.append(my_list1[i] / my_list2[i])
        except exceptions as el:
            print(e)
        finally:
            return new_list
