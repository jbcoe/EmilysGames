import sys
import random

words = 'cat cot top pot tin tan not pat put pit tip inn mop dog got'.split()

choices = 3

def main():
    score = 0
    while score < 100:
        
        word = random.choice(words)
        others = random.sample([w for w in words if w is not word], choices)

        print "================================================"
        print "Find a word like \"{}\"".format(word)
        print "================================================"

        for i,w in enumerate(others):
            print "{}: {}".format(i,w)
            print "   {}\n".format(word)
	print "================================================"
        
        while True:
            input = raw_input() 
            try:
                index = int(input)
                if index > len(others) or index < 0:
                    raise Exception('out of range input')
                w = others[index]
                common = []
                for x,y in zip(sorted(word), sorted(w)):
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
