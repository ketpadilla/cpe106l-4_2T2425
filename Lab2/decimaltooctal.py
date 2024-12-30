""" 
  LAB 02
  INLAB 03
  
  Octal numbers have a base of eight and the digits 0-7. Write the scripts octaltodecimal.py and decimaltooctal.py, which convert numbers between the octal and decimal representations of integers. These scripts use algorithms that are similar to those of the binaryToDecimal and decimalToBinary scripts developed in Section 4-3. (LO: 4.1, 4.3)

  Credits: Fundamentals of Python: First Programs Chapter 04
"""

from includes.clear import clearSYS

def decimal_to_octal(decimalNum):
    if decimalNum == 0:
        return "0"
    octalNum = ""
    while decimalNum > 0:
        remainder = decimalNum % 8
        octalNum = str(remainder) + octalNum # from rightmost digit to leftmost digit
        decimalNum = decimalNum // 8
    return octalNum

def main():
  clearSYS()
  
  decimalNumber = int(input("Enter a decimal number: "))
  octalNumber = decimal_to_octal(decimalNumber)
  print(f"Decimal Number: {decimalNumber} ==> Octal Number: {octalNumber}")
  return 0

if __name__ == "__main__":
    main()
