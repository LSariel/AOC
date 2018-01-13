

# Problem one: Not solved yet. Answer too high.
def prob1(listxlist):
    result = 0
    for line in listxlist:
        valid = True
        words = []
        for word in line:
            for oldword in words:
                if word == oldword:
                    valid = False
            words.append(word)
        if valid:
            result += 1
    return result


def main():
    passphrases = []
    with open('day_4_input.txt') as inputfile:
        for line in inputfile:
            passphrases.append(line.rstrip().split('\t'))
    print "Day 4 puzzle 1: " + str(prob1(passphrases))


if __name__ == '__main__':
    main()