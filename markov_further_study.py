from random import choice
from sys import argv
import string


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_file = open(file_path)

    return text_file.read()


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    
    chains = {}
    i = 0
    text_string = text_string.strip()
    text_string = text_string.split()

    # your code goes here
    while i < len(text_string) - 2:
        bi_gram = (text_string[i], text_string[i + 1])

        if chains.get(bi_gram) is None:
            chains[bi_gram] = [text_string[i + 2]]
        else:
            chains[bi_gram] = chains.get(bi_gram) + [(text_string[i + 2])]
        i += 1

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    master_text = ()
    # master_text = [item for item in chains while (item[0][0] in string.ascii_uppercase and master_text == ())]
    while master_text == ():
        for item in chains:
            if item[0][0] in string.ascii_uppercase:
                master_text = item
    text = [master_text[0], master_text[1]] #figure out how to have a tuple item[0], item[1]

    while chains.get(master_text) is not None:  #and also ends on punctuation mark
        next_word = choice(chains.get(master_text))
        text.append(next_word)
        master_text = (text[-2], text[-1])

    # your code goes here


    return ' '.join(text)



input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
 
# Produce random text
random_text = make_text(chains)

print random_text
