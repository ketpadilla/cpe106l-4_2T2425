""" 
  LAB 02
  PROGRAMMING PROBLEM 02

  Write a program that allows the user to navigate through the lines of text in a file. The program prompts the user for a filename and inputs the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.

  *The following program was mostly copied (with minor revisions) from PostLabSolution2.py (https://github.com/ketpadilla/cpe106l-4_2T2425/blob/main/Lab1/PostLabSolution2.py) as they have the same problem.
"""

from includes.clear import clearSYS
import os
import platform 

# ANSI color codes
CYAN = '\033[36m'
BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'
DARK_GRAY = '\033[1;30m'

def main():
  # get, validate and open file
  while True:
    try:
      clearSYS()

      fn = input("Input file name (sample.txt, empty.txt, or full path, or 'X' to quit)\n:: ")

      if fn.upper() == "X": 
        print(YELLOW + "Quitting" + RESET + " program.")
        return 0

      file_path = os.path.join("exp01/includes/",fn) if not os.path.isabs(fn) else fn
      with open(file_path, 'r') as file:
        data = file.readlines()

      # prompt empty file
      if not data:
        input("\nThe file is " + RED + "empty." + RESET + "\nPress " + YELLOW + "Enter" + RESET + " to try another file.")
        continue
      break

    except:
      input("\n" + RED + "Invalid" + RESET + " input.\nPress " + YELLOW + "Enter" + RESET + " and try again.")

  lines = len(data)
  while True:
    clearSYS()

    # print the number of lines and prompt for user input
    print("Number of lines in " + CYAN + f"{fn}" + RESET + ": " + GREEN + f"{lines}\n" + RESET)
    line = input("What " + BLUE + "line" + RESET + " do you want to print? (Enter 0 to exit)\n:: ")

    # validate input
    try: 
      line = int(line)

    except:
      input("\n" + RED + "Invalid" + RESET + " input.\nPress " + YELLOW + "Enter" + RESET + " and try again.")
      continue

    if line == 0:
       break

    if line > lines or line < 1: 
      input( RED + "\nOut" + RESET + " of bounds.\nPress " + YELLOW + "Enter" + RESET + " to continue.")
      continue

    # access and print line contents
    content = data[line - 1].rstrip()
    if not content:
      print(DARK_GRAY + "\n\tEmpty line" + RESET)
    else: 
      print(BLUE + f"\n\t{data[line - 1].rstrip()}" + RESET)

    input("\nPress " + YELLOW + "Enter" + RESET + " to continue.")

  # end program
  clearSYS()
  print(YELLOW + "Quitting" + RESET + " program.")
  return 0

main()