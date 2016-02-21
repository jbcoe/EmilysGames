import sys
import subprocess
import random
from getchar import *

#
# This program has been written to run on raspberry pi so probably runs only on Linux.
# You will need figlet installed to print big letters to the console.
# To install figlet run: 
# sudo apt-get install figlet
#

def big_print(message):
    command = ['figlet']
    command.extend(message.split())
    subprocess.call(command)

letters = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

def main():
    while len(letters) != 0:
        letter = random.choice(letters)
        letters.remove(letter)
     
        subprocess.call(['clear'])
        big_print("{}".format(letter))
        while True:
            input = getch() 
            if str(input).upper() == letter:
                break
    
    big_print("* You win! *")

if __name__ == '__main__':
    main()
