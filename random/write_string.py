import random

'''Write a function that shows the likelihood of generating the inputted string'''

def write_string(strlen):
    # use accumulator pattern
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res = ''
    for i in range(strlen):
        res += alphabet[random.randrange(27)]

    return res

def score(goal, teststring):
    num_same = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            num_same += 1
    return num_same / len(goal)

def main():
    goalstring = 'i think therefore i'
    best = 0
    new_string = write_string(20)
    new_score = score(goalstring, new_string)
    while new_score < 1:
        if new_score >= best:
            print(new_score, new_string)
            best = new_score
        new_string = write_string(20)
        new_score = score(goalstring, new_string)

main()

