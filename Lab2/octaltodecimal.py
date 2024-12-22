""" 
  LAB 02
  INLAB 03
  
  Octal numbers have a base of eight and the digits 0-7. Write the scripts octaltodecimal.py and decimaltooctal.py, which convert numbers between the octal and decimal representations of integers. These scripts use algorithms that are similar to those of the binaryToDecimal and decimalToBinary scripts developed in Section 4-3. (LO: 4.1, 4.3)

  Credits: Fundamentals of Python: First Programs Chapter 04
"""

from includes.clear import clearSYS

def octal_to_decimal(octalNum):
    decimalNumber = 0
    power = 0 

    for digit in reversed(octalNum):
        if int(digit) >= 8:
            raise ValueError("Invalid octal number")
        decimalNumber += int(digit) * 8**power
        power += 1

    return decimalNumber

def main():
  clearSYS()
  
  octalNumber = input("Enter an octal number: ")
  decimalNumber = octal_to_decimal(octalNumber)
  print(f"Octal number: {octalNumber} ==> Decimal Number: {decimalNumber}")

  return 0

if __name__ == "__main__":
    main()
