""" 
  LAB 02
  INLAB 01
  
  Write a script in the file encrypt.py that inputs a line of plaintext and a distance value and outputs an encrypted text using a Caesar cipher. The script should work for any printable characters. (LO: 4.1, 4.2)

  Credits: Fundamentals of Python: First Programs Chapter 04
"""

from includes.clear import clearSYS

# ANSI color codes
RESET = '\033[0m'
YELLOW = '\033[33m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'

def encrypt(plaintext, dist):
  ciphertext = []
  for c in plaintext: 
    if c.isalpha(): # Ceasar cipher encryption logic
      base = ord('A') if c.isupper() else ord('a') 
      ciphertext.append(chr((ord(c) - base + dist) % 26 + base)) 
    else: ciphertext.append(c)
  return ''.join(ciphertext) # convert list into a string

def main():
  clearSYS()

  # get plaintext
  plaintext = input("Enter " + YELLOW + "plaintext" + RESET + " or " + RED + "X" + RESET + " to exit\n:: ")
  if plaintext == "X":
    print(YELLOW + "Quitting" + RESET + " program.")
    return 0

  # get distance value
  while True:
    try:
      dist = int(input("\nEnter " + GREEN + "distance" + RESET + " value\n:: "))
      break
    except:
      input("\n" + RED + "Invalid" + RESET + " input.\nPress " + YELLOW + "Enter" + RESET + " and try again.")

  # encrypt and print plaintext
  ciphertext = encrypt(plaintext, dist)
  print("\nMessage: " + YELLOW + plaintext + RESET)
  print("Ciphertext (shift of " + GREEN + f"{dist}" + RESET + "): " + CYAN + ciphertext)
  return 0

if __name__ == "__main__":
    main()