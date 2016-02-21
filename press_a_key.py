import sys
import subprocess
import random
from getchar import *

def big_print(message):
  command = ['figlet']
  command.extend(message.split())
  subprocess.call(command)

letters = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

while len(letters) != 0:
  letter = random.choice(letters)
  letters.remove(letter)
  while True:
    big_print("Press '{}'".format(letter))
    input = getch() 
    if str(input).upper() == letter:
      subprocess.call(['clear'])
      big_print("Well done!")
      break
    else:
      print "Try again Emily."

big_print("* You win! *")

