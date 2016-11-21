import sys
import random

_words = 'cat cot top pot tin tan not pat put pit tip inn mop dog got'.split()
_choices = 3
_score = 0


def generate_word_and_matches():
    word = random.choice(_words)
    others = random.sample([w for w in _words if w is not word], _choices)
    return word, others


def calculate_points(word, match):
    common = [w for w in match if w in word]
    points = len(common)
    return points, common


def get_score():
    global _score
    return _score


def reset_score():
    global _score
    _score = 0


def increase_score(points):
    global _score
    _score = _score + points


def _index_input(r, options):
    try:
        input = r()
        index = int(input)
        if index >= len(options) or index < 0:
            raise Exception('out of range input')
        return index
    except:
        return None


def main():
    reset_score()
    while get_score() < 100:
        word, others = generate_word_and_matches()

        print "================================================"
        print "Find a word like \"{}\"".format(word)
        print "================================================"

        for i, w in enumerate(others):
            print "{}: {}".format(i, w)
        print "================================================"

        index = None
        while index == None:
            print "Pick {}".format(" or ".join([str(x) for x in xrange(len(others))]))
            index = _index_input(raw_input, others)
        w = others[index]
        points, common = calculate_points(word, w)
        increase_score(points)

        print "\"{}\" and \"{}\" have \"{}\" in common".format(word, w, ",".join(common))
        print "You score {} new points".format(points)
        print "================================================"
        print "Your score is {}".format(get_score())

    print "================================================"
    print " *** CONGRATULATIONS Emily! You win! ***"
    print "================================================"


if __name__ == '__main__':
    main()
