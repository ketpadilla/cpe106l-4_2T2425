
""" 
  LAB 02
  INLAB 04
  
  Write a program in the file unique.py that inputs a text file. 
  The program should print the unique words in the file in alphabetical order. (LO: 5.1)

  Credits: Fundamentals of Python: First Programs Chapter 05
"""

from includes.clear import clearSYS

def getUnique(filename):
    unique_words = set()
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                unique_words.add(word)
  
 
    return sorted(unique_words)

def main():
    clearSYS() 
  
    filename = input("Enter the name of the file (includes/[filename]): ")
    unique_words = getUnique(filename)

    print("Unique words in alphabetical order:")
    for word in unique_words:
            print(word)

    return 0

if __name__ == "__main__":
    main()


