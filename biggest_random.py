#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: June 2022
# This program finds the largest of 10 random numbers

import random


def biggest(lists):
    # this function finds the largest in the list
    biggest = lists[0]
    list_counter = 0

    while list_counter < len(lists):
        if lists[list_counter] > biggest:
            biggest = lists[list_counter]

        list_counter = list_counter + 1

    return biggest


def main():

    random_numbers = []

    loop_counter = 0

    print("Here are the 10 numbers:")

    while loop_counter < 10:
        random_variable = random.randint(0, 100)
        random_numbers.append(random_variable)
        loop_counter = loop_counter + 1
    print("")

    # call function
    some_var = biggest(random_numbers)

    print(random_numbers)
    print("\nThe biggest of these 10 numbers is {}".format(some_var))

    print("\nDone.")


if __name__ == "__main__":
    main()
