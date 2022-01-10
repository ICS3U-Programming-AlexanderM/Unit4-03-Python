#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Jan 10 2022
# This program asks the user to enter a number
# and then uses a loop to calculate and display the square
# of numbers between 0 and the user's number.

def main():
    # get the user input
    user_string = input("Enter your number: ")
    print("")

    # check inputs
    try:
        user_number = int(user_string)
    except Exception:
        print("Invalid input, must be an integer.")
    else:
        # check if number is negative
        if user_number < 0:
            print("Number cannot be negative.")
        else:
            # calculate the squares
            for loop in range(user_number + 1):
                square = loop ** 2
                print("{} ^ 2 = {}". format(loop, square))
    finally:
        # finalize program
        print("")
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
