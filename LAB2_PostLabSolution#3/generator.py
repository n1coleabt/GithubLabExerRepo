"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random
import string

def getWords(fileName):
    f = open(fileName, 'r');
    # Input the text, convert it to numbers, and
    # add the numbers to a list
    tempList = []
    for line in f:
        words = line.split()
        for word in words:
            tempList.append(word)

    tupleList = tuple(tempList)
    return tupleList

nouns = getWords("LAB2_PostLabSolution#3/nouns.txt");
verbs = getWords("LAB2_PostLabSolution#3/verbs.txt");
articles = getWords("LAB2_PostLabSolution#3/articles.txt");
prepositions = getWords("LAB2_PostLabSolution#3/prepositions.txt");

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()

