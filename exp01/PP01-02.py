""" 
  EXPERIMENT 01
  PROGRAMMING PROBLEM 02

  Write a program that allows the user to navigate through the lines of text in a file. The program prompts the user for a filename and inputs the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.
"""

import os
import platform

def main():
  # Clear system
  if platform.system() == "Windows": os.system('cls')
  else: os.system('clear')
  
  # TODO

main()