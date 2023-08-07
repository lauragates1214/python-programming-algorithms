"""
    PROGRAM :  Felipe's Taqueria
    AUTHOR  :  Laura Purcell-Gates
    EMAIL   :  <laurapurcellgates@gmail.com>

    CS50P 2023 Problem Set 3 Felipe's Taqueria

    Felipe's Taqueria is a program that enables a user to place an order, validates inputs against
    a menu dictionary, and displays the total cost of all items inputted thus far, until the user
    inputs control-d.

    Code fully written by me; no pre-filled CS50 code.

    Link to the problem set:
    https://cs50.harvard.edu/python/2022/psets/3/taqueria/  """


def main():
    # create dictionary to store menu items
    menu = {
        'Baja Taco': 4.00,
        'Burrito': 7.50,
        'Bowl': 8.50,
        'Nachos': 11.00,
        'Quesadilla': 8.50,
        'Super Burrito': 8.50,
        'Super Quesadilla': 9.50,
        'Taco': 3.00,
        'Tortilla Salad': 8.00
    }
    # set price variable to 0.00
    price = 0.00
    # call order function
    order(menu, price)
    return


def order(d, price):
    # ask user for input, case insensitive, convert to title case
    try:
        item = input('Order: ').lower().title()
        # use d[key] to return value of food item
        try:
            price += d[item]
            print(f'Total: ${price:.2f}')
            order(d, price)
        except KeyError:
            order(d, price)
    except EOFError:
        print('\n')
        return


if __name__ == '__main__':
    main()
