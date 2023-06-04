"""
    PROGRAM :  Credit
    AUTHOR  :  Laura Purcell-Gates
    EMAIL   :  <laurapurcellgates@gmail.com>

    CS50x 2023 Problem Set 6 Credit

    Credit is a program that prompts the user for a credit card number,
    then uses Luhn's algorithm to validate the card number as Visa, MasterCard,
    American Express or invalid.

    I also wrote it in C as part of CS50x Problem Set 1
    (see Harvard-CS50-labs-problemsets-C repository).

    Code fully written by me; no pre-filled CS50 code.

    Link to the problem set:
    https://cs50.harvard.edu/x/2023/psets/6/credit/  """


from cs50 import get_int


def main():
    # prompt user for number
    number = user_prompt()

    # calculate total1
    # (sum of digits of second to last digit & every other *2)
    number1 = int(number / 10)
    total1 = 0
    while number1 > 1:
        digit = (int(number1 % 10)) * 2
        if digit > 9:
            digit1 = int(digit % 10)
            digit2 = int((digit / 10) % 10)
            digit = digit1 + digit2
        total1 += digit
        number1 /= 100

    # calculate total2
    # (sum of other numbers)
    number2 = int(number)
    total2 = 0
    while number2 > 1:
        digit = int(number2 % 10)
        total2 += digit
        number2 /= 100

    # add total1 to total2
    final = total1 + total2

    # run card = checks(number)
    card = checks(number, final)

    # print result
    print(card)


def user_prompt():
    number = 0
    while number <= 0:
        number = get_int("Number: ")
    return number


def checks(number, final):
    # run checks; return card
    div13 = amex = int(number / 10**13)
    div15 = visa16 = int(number / 10**15)
    div16 = int(number / 10**16)
    visa13 = int(number / 10**12)
    mc = int(number / 10**14)

    if final % 10 == 0:
        # check VISA 13-digit starting 4
        if div13 <= 1 and visa13 == 4:
            return ("VISA")

        # check AMEX 15-digit starting 34 or 37
        elif div15 <= 1 and (amex == 34 or amex == 37):
            return ("AMEX")

        # check MC 16-digit starting 5
        elif div16 <= 1 and (mc == 51 or mc == 52 or mc == 53 or mc == 54 or mc == 55):
            return ("MASTERCARD")

        # check VISA 16-digit starting 4
        elif div16 <= 1 and visa16 == 4:
            return ("VISA")

        # if none of the above, INVALID
        else:
            return ("INVALID")

    else:
        return ("INVALID")


if __name__ == "__main__":
    main()