""" 
  LAB 02
  INLAB 05
  
  A file concordance tracks the unique words in a file and their frequencies. 
  Write a program in the file concordance.py that displays a concordance for 
  a file. The program should output the unique words and their frequencies in 
  alphabetical order. Variations are to track sequences of two words and their 
  frequencies, or n words and their frequencies. (LO: 5.3)

  Credits: Fundamentals of Python: First Programs Chapter 05
"""

from includes.clear import clearSYS

def getConcordance(filename):

    with open(filename, "r") as input_file:
        text = input_file.read().lower()
  
    words = text.split()
    concordance = {}

    for word in words:
        word = ''.join(filter(str.isalnum, word))
        if word in concordance:
            concordance[word] += 1
        else:
            concordance[word] = 1

    return sorted(concordance.items())

def main():
    clearSYS() 
  
    filename = input("Enter the name of the file (includes/[filename]): ")
    concordance = getConcordance(filename)

    for word, frequency in concordance:
        print(f"{word}: {frequency}")
    return 0

if __name__ == "__main__":
    main()
