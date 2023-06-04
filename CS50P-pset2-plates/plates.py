"""
    PROGRAM :  Vanity Plates
    AUTHOR  :  Laura Purcell-Gates
    EMAIL   :  <laurapurcellgates@gmail.com>

    CS50P 2023 Problem Set 2 Vanity Plates

    Vanity Plates is a program that validates a vanity plate entered by the user
    against four Massachusettes vanity plate requirements.

    Code fully written by me; no pre-filled CS50 code.

    Link to the problem set:
    https://cs50.harvard.edu/python/2022/psets/2/plates/  """


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    # check that string is only alphanumeric
    if str.isalnum():
        # check for valid string length
        if len(str) <= 6 and len(str) >= 2:
            # all letters within valid string length returns valid
            if str.isalpha():
                return True
            # if not all alpha, check starts with at least 2 letters
            elif str[0:2].isalpha():
                # iterate through string
                for c in str:
                    # find first number
                    if c.isnumeric():
                        # create variable to store latter part of string if contains numbers
                        num_test = ""
                        # store latter part of string in variable
                        num_test = str[(str.index(c)) + 1: len(str)]
                        # check for invalid number conditions
                        if c == "0" or str[-1].isdigit() == False or num_test.isnumeric() == False:
                            return False
                        # all tests for plate containing number passed
                        else:
                            return True
    # test failed (if conditions above)
    return False


if __name__ == "__main__":
    main()