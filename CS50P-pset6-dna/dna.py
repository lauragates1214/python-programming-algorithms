"""
    PROGRAM :  DNA
    AUTHOR  :  Laura Purcell-Gates
    EMAIL   :  <laurapurcellgates@gmail.com>

    CS50x 2023 Problem Set 6 DNA

    DNA is a program that identifies a person based on their DNA.

    My contributions to the code commented as LauraPG (main function).

    Link to the problem set:
    https://cs50.harvard.edu/x/2023/psets/6/dna/  """


import csv
import sys


def main():

    # LauraPG: Check for command-line usage
    if len(sys.argv) != 3:
        print('Please enter the correct number of files')
        return

    # LauraPG: Read database & sequence files into variables
    csvFilename = sys.argv[1]
    txtFilename = sys.argv[2]

    # LauraPG: open sequence file
    txtReader = open(txtFilename, 'r')

    # LauraPG: assign variable to contents of file
    sequence = txtReader.read()

    # LauraPG: initialize list for names
    names = []

    # LauraPG: create reader object for file
    with open(csvFilename) as csvFile:
        csvReader = csv.DictReader(csvFile)

        # LauraPG: loop through reader to append name & occurrences
        for person in csvReader:
            names.append(person)

    # LauraPG: Find longest match of each STR in DNA sequence
    # LauraPG: initialize list to store STR counts
    STRcounts = []
    # LauraPG: initialize variable to store dicts in names
    STRdict = {}

    # LauraPG: loop through STRs from database, send to longest_match function
    STRnum = len([*names[0]])
    for i in range(1, STRnum):
        STRcounts.append(longest_match(sequence, ([*names[0]][i])))

        # LauraPG: Check database for matching profiles
        # LauraPG: loop through dicts in names
        for dict in names:
            # LauraPG: add each dict to STRdict
            STRdict.update(dict)
            # LauraPG: initialize list variable to store dict values
            STRperson = list(STRdict.values())
            # LauraPG: remove name value from list
            STRperson.pop(0)
            # LauraPG: convert remaining values to ints
            STRperson_ints = [eval(i) for i in STRperson]
            # LauraPG: compare to STRcounts
            if STRcounts == STRperson_ints:
                print(STRdict['name'])
                return

    # LauraPG: print & return
    print('No match')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
