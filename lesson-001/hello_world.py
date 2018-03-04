#!/usr/bin/env python
# https://docs.python.org/2/library/sys.html
import sys

# This line is a comment line

""" This
is a multiline
comment
"""

#"""
# Needs Improvement... There is a better way!
print (
    "Hello " 
    + sys.argv[0]
    + "!, my child is " 
    + str(len(sys.argv))
    + " years old...")
#"""

"""
# This is an improvement, but what if you need to add new variables often, or reorder them...
print (
    "Hello {}!, my child is {} years old...".format(
        sys.argv[0],
        len(sys.argv)
    )
)
"""


"""
# This is much better and more self documenting. 
# Adding new variables to the string and reordering the variables is no problem at all.
print (
    "Hello {program_name}!, my child is {argument_length} years old...".format(
        program_name = sys.argv[0],
        argument_length = len(sys.argv)
    )
)
"""

"""
 Homework:
 * Study the two functions below. Try to determine what they do before calling them.
 * Fill in the your_code_here function so that it prints the same string as before but
     also ensure that it prints your program name formatted to a more readable human name,
 * Call interesting_function with as many different data types as possible
     e.g. integer, string, etc, library name (sys), etc.
 * format_program_name_as_human_name is an example of a "one-liner". 
     Imagine what it would look like broken into each of it's operations, one per line...
     Write a one-liner function "is_str(o)" that returns true if an object is of type string, and false otherwise.
       Hints:
         https://mail.python.org/pipermail/python-dev/2005-September/056846.html
         https://docs.python.org/2/library/functions.html
         https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
"""

def format_program_name_as_human_name(program_name): 
    return program_name.split('.')[1][1:].title().replace("_", " ")

def interesting_function(o):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint (dir(o)) 
    
#print(format_program_name_as_human_name(sys.argv[0]))
#interesting_function(1)

def your_code_here():
    pass
     