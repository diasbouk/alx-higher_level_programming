#!/usr/bin/pytohn3
def list_division(my_list1, my_list2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list1[i] / my_list2[i]
        except IndexError:
            result = 0
            print("out of range")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        finally:
            new_list.append(result)
    return new_list
