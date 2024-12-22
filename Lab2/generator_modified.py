"""
  LAB 02
  PROGRAMMING PROBLEM 03

  Write a program that allows the user to navigate through the lines of text in a file. The program prompts the user for a filename and inputs the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.
  
  CREDITS
  Program: generator.py
  Author: Ken
  Generates and displays sentences using a simple grammar
  and vocabulary.  Words are chosen at random.
"""

from includes.clear import clearSYS
import random
import os

def getWords(filename):
    """Reads words from a file and returns them as a tuple"""
    with open(filename, 'r') as file:
        words = [line.strip() for line in file] # one word per line
    return tuple(words)

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

"""Initialize vocabulary from files."""
base_path = "Lab2/includes"
nouns = getWords(os.path.join(base_path, "nouns.txt"))
verbs = getWords(os.path.join(base_path, "verbs.txt"))
articles = getWords(os.path.join(base_path, "articles.txt"))
prepositions = getWords(os.path.join(base_path, "prepositions.txt"))

def main():
    """Allows the user to input the number of sentences
    to generate."""

    clearSYS()
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    """Program's entry point."""
    main()