"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic2 import *
from functools import reduce

# def token_string(sen):
#     """ tokenizing the input"""
#     tokens = sen.split(" ")
#     return tokens

def run_calculator():

    while True:
        user_input = input("> ")

        tokens = user_input.split(" ")
        operator = tokens[0]


        if operator == "q":
            break

        numbers = convert_nums_to_floats(tokens[1:])


        if operator == "+":
            print(add(numbers))
        elif operator == "-":
            print(subtract(numbers))
        # elif tokens[0] == "*":
        #     print(multiply(float(tokens[1]), float(tokens[2])))
        # elif tokens[0] == "/":
        #     print(divide(float(tokens[1]), float(tokens[2])))
        # elif tokens[0] == "square":
        #     print(square(float(tokens[1])))
        # elif tokens[0] == "cube":
        #     print(cube(float(tokens[1])))
        # elif tokens[0] == "pow":
        #     print(power(float(tokens[1]), float(tokens[2])))
        # elif tokens[0] == "mod":
        #     print(mod(float(tokens[1]), float(tokens[2])))
            

def convert_nums_to_floats(li):
    """List -> List. Takes in tokenized input and converts everything into floats
    """
    floatified = []
    for number in li:
        floatified.append(float(number))
    return floatified



run_calculator()


