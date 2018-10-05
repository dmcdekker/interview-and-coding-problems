import unittest

def min_bribes(queue):
    
    ql = len(queue)
    swap = 0
    swapped = True
    
    # fail fast if too chaotic
    for i in queue:
        index = queue.index(i)
        if (i - index) > 3:
            print("Too chaotic")
            return    
        
    # starting at the end of the list iterate through list and count swaps
    j = 0
    while swapped:
        j += 1
        # no swap in the previous iteration, there is no need to run a new swap iteration
        swapped = False
        for i in range(ql - j):
            if queue[i] > queue[i+1]:
                # swap elements
                queue[i], queue[i+1] = queue[i+1], queue[i]
                swap += 1
                swapped = True

    print(swap)
    return swap

# alt solution
def minimum_bribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i) > 3:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes) 
    return bribes     


class Test(unittest.TestCase):

    def test_min_bribes_1(self):
        actual = min_bribes([2, 1, 5, 3, 4])
        expected = 3 
        self.assertEqual(actual, expected)

    def test_min_bribes_2(self):
        actual = min_bribes([2, 5, 1, 3, 4])
        expected = None
        self.assertEqual(actual, expected)


    def test_min_bribes_3(self):
        actual = minimum_bribes([2, 1, 5, 3, 4])
        expected = 3 
        self.assertEqual(actual, expected)

    def test_min_bribes_4(self):
        actual = minimum_bribes([2, 5, 1, 3, 4])
        expected = None
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)