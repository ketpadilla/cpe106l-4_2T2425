""" 
  EXPERIMENT 01
  PROGRAMMING PROBLEM 01

  Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. The median is the number that would appear at the midpoint of a list if it were sorted. The mode is the number that appears most frequently in the list. Define these functions in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers. Each function expects a list of numbers as an argument and returns a single number.  
"""

import includes.stats as sts
from includes.clear import clearSYS
import os

def main():
  clearSYS()
  
  # Call sample function
  sts.hello()

main()