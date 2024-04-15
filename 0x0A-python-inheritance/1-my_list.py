#!/usr/bin/python3

"""
Modules docs (if any)
"""

class MyList(list):
    """
    Class representing a list

    """
    def print_sorted(self):
        """
        prints a sorted list
        dosent sort the original list
        """
        print(sorted(list(self)))
