"""
    PROGRAM :  Readability
    AUTHOR  :  Laura Purcell-Gates
    EMAIL   :  <laurapurcellgates@gmail.com>

    CS50x 2023 Problem Set 6 Readability

    Readability is a program that calculates the approximate grade
    reading level for a text using the Coleman-Liau index.

    I also wrote it in C as part of CS50x Problem Set 2
    (see repository for C labs and problem sets from Harvard CS50).

    Code fully written by me; no pre-filled CS50 code.

    Link to the problem set:
    https://cs50.harvard.edu/x/2023/psets/6/readability/  """


from cs50 import get_string


def main():
    # prompt user for text input
    text = get_string('Text: ')

    # call count_letters function
    total_letters = count_letters(text)

    # call count_words function
    total_words = count_words(text)

    # call count_sentences function
    total_sentences = count_sentences(text)

    # calculate L (avg number of letters per 100 words)
    L = (total_letters / total_words) * 100

    # calculate S (avg number of sentences per 100 words)
    S = (total_sentences / total_words) * 100

    # run Coleman-Liau index: index = 0.0588 * L - 0.296 * S - 15.8
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # print grade level
    if index >= 16:
        print('Grade 16+')
    elif index < 1:
        print('Before Grade 1')
    else:
        print(f'Grade {index}')


def count_letters(text):
    # initialize lettercount to 0
    lettercount = 0

    # for loop to iterate through each character in text
    for char in text:
        # check for alpha
        if char.isalpha():
            # count letters, assign to letter_count
            lettercount += 1

    # return lettercount
    return (lettercount)


def count_words(text):
    # initialize wordcount to 0
    wordcount = 0

    # count words using ASCII 32 [space] to mark word endings
    for char in text:
        if ord(char) == 32:
            wordcount += 1

    # add 1 to wordcount (bc final word will end with punctuation or no space)
    wordcount += 1

    # return wordcount
    return (wordcount)


def count_sentences(text):
    # initialize sentencecount to 0
    sentencecount = 0

    # count sentences using '.', '!' or '?' as stopping points
    for char in text:
        if char == '.' or char == '!' or char == '?':
            sentencecount += 1

    # return sentencecount
    return (sentencecount)


if __name__ == "__main__":
    main()
