"""
    PROGRAM :  Outdated
    AUTHOR  :  Laura Purcell-Gates
    EMAIL   :  <laurapurcellgates@gmail.com>

    CS50P 2023 Problem Set 3 Outdated

    Outdated is a program that prompts the user for a date, Anno Domini, in MM-DD-YYYY order,
    formatted like 9/8/1636 or September 8, 1636, with validation checks. It then outputs that
    same date in YYYY-MM-DD format.

    Code fully written by me; no pre-filled CS50 code.

    Link to the problem set:
    https://cs50.harvard.edu/python/2022/psets/3/outdated/  """


def main():
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    # prompt user for input
    date = input('Date: ').lower().title().strip()
    # call date conversion function
    print(conversion(date, months))


def conversion(date, months):
    # split string by either '/' or ' '
    try:
        if date.find('/') != -1:
            numbers = date.split('/')
            # assign month
            month = numbers[0]
        elif date.find(',') == -1:
            main()
        else:
            numbers = date.replace(',', '').split(' ')
            # convert text month to number, reprompt if not in months list
            try:
                month = str(months.index(numbers[0]) + 1)
            except:
                main()
    except:
        main()
    # assign day and year
    day = numbers[1]
    year = numbers[2]
    # validation checks
    if len(month) > 2 or len(month) < 1 or int(month) == 0 or int(month) > 12 or len(day) > 2 or len(day) < 1 or int(day) == 0 or int(day) > 31 or len(year) != 4:
        main()
    else:
        # convert numbers to integers
        year = int(year)
        month = int(month)
        day = int(day)
        # return reformatted date to main()
        return(f'{year}-{month:02}-{day:02}')


if __name__ == '__main__':
    main()