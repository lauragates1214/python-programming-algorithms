"""
    PROGRAM :  Grocery List
    AUTHOR  :  Laura Purcell-Gates
    EMAIL   :  <laurapurcellgates@gmail.com>

    CS50P 2023 Problem Set 3 Grocery List

    Grocery List is a program that prompts the user for grocery list items, one per line,
    until the user inputs control-d. It then outputs the grocery list in all uppercase,
    sorted alphabetically by item, prefixing each line with the number of times the user
    inputted that item.

    Code fully written by me; no pre-filled CS50 code.

    Link to the problem set:
    https://cs50.harvard.edu/python/2022/psets/3/grocery/  """


def main():
    # create grocery list dictionary
    grocery_list = dict()
    # call function that starts adding to grocery list
    add_groceries(grocery_list)
    # print alphabetized grocery list, with counter values
    # & one line break at start
    print()
    for key, value in sorted(grocery_list.items()):
        print(value, key)
    return


def add_groceries(d):
    # ask user for grocery list item, add to list
    try:
        item = input('').upper()
    except EOFError:
        # return grocery_list to main()
        return d
    # run item through counter
    counter = 0
    if d.get(item) == None:
        d[item] = 1
        add_groceries(d)
    else:
        counter = d[item] + 1
        d.update({item: counter})
        add_groceries(d)


if __name__ == '__main__':
    main()



