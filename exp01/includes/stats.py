#stats.py

from collections import Counter

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_number = sorted(numbers)
    size = len(numbers)

    mid = size // 2

    if size % 2 == 0:
        almost_mid = (sorted_number[mid] + sorted_number[mid - 1])
        return almost_mid / 2
    else:
        return sorted_number[mid]

def mode(numbers):
    if not numbers:
        raise ValueError("The input list is empty")

    counts = Counter(numbers)
    max_count = max(counts.values())

    modes = []
    for num, count in counts.items():
        if count == max_count:
            modes.append(num)
    
    # return a single mode if there is only one, otherwise return the list of modes
    if len(modes) == 1:
        return modes[0]
    else:
        return modes