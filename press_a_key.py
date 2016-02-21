import sys
import subprocess
import random
from getchar import *

def big_print(message):
  subprocess.call(['clear'])
  command = ['figlet']
  command.extend(message.split())
  subprocess.call(command)

letters = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

while len(letters) != 0:
  letter = random.choice(letters)
  letters.remove(letter)
  while True:
    print "Press the letter '{}'".format(letter)
    input = getch() 
    if input == 'Q':
      print "Bye"
      sys.exit(0)
    elif str(input).upper() == letter:
      big_print("Well done Emily!")
      break
    elif input == '\n':
      continue
    else:
      print "Try again Emily."

if len(letters) == 0:
  big_print("You win, Emily!")

