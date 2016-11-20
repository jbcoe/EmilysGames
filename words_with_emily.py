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

words = 'cat cot top pot tin tan not pat put pit tip inn mop dog got'.split()

def main():
    score = 0
    while score < 100:
        
        word = random.choice(words)
        others = random.sample([w for w in words if w is not word], 5)

        print "================================================"
        print "Find the best match for \"{}\"".format(word)
        print "================================================"

        for i,w in enumerate(others):
            print "{}: {}".format(i,w)
        print "================================================"
        
        while True:
            input = getch() 
            try:
                index = int(input)
                if index > len(others) or index < 0:
                    raise Exception('out of range input')
                w = others[index]
                common = []
                for x,y in zip(word, w):
                    if x == y: common.append(x)
                points = len(common)
                
                print "\"{}\" and \"{}\" have \"{}\" in common".format(word, w, ",".join(common))
                print "You score {} new points".format(points)
                print "================================================"
                score = score + points
                print "Your score is {}".format(score)
            except:
                continue
            break

    print "================================================"
    print " *** CONGRATULATIONS Emily! You win! ***"
    print "================================================"


if __name__ == '__main__':
    main()
