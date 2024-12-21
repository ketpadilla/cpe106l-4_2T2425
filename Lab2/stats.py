""" 
  EXPERIMENT 02
  PROGRAMMING PROBLEM 01
  
  Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. The median is the number that would appear at the midpoint of a list if it were sorted. The mode is the number that appears most frequently in the list. Define these functions in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers. Each function expects a list of numbers as an argument and returns a single number.
"""

from collections import Counter
from includes.clear import clearSYS
import os

def main():
    clearSYS()
    print("Enter a list of numbers separated by spaces:")
    numbers = list(map(float, input().split()))

    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print(f"Mode: {mode(numbers)}")

def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    size = len(numbers)
    mid = size // 2

    if size % 2 == 0:
        return (sorted_numbers[mid] + sorted_numbers[mid - 1]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    if not numbers:
        raise ValueError("The input list is empty")

    counts = Counter(numbers)
    max_count = max(counts.values())

    modes = [num for num, count in counts.items() if count == max_count]
    
    # return a single mode if there is only one, otherwise return the list of modes
    if len(modes) == 1:
        return modes[0]
    else:
        return modes
main()
