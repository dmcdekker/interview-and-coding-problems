import unittest

def minimum_swaps(a):
    '''Find the minimum number of swaps needed to order list of nums'''

    # declare dict for values in list
    m = {}
    # add values to dict with index position
    for i in range(len(a)):
        m[a[i]] = i 
      
    # make copy of sorted list
    sorted_list = sorted(a)
    swaps = 0
    
    # iterate through list and compare index positions of values
    for i in range(0, len(a)):
        
        if a[i] != sorted_list[i]:
   
            # increment swaps int
            swaps += 1
          
            # get index of the sorted value from dict
            ind_to_swap = m[sorted_list[i]]

            # update value of current list elem with sorted list value
            m[a[i]] = m[sorted_list[i]]
            
            # swap list current value with sorted value
            a[i], a[ind_to_swap] = sorted_list[i], a[i]
           
    return swaps

class Test(unittest.TestCase):

    def test_min_swaps_1(self):
        actual = minimum_swaps([4, 3, 1, 2])
        expected = 3 
        self.assertEqual(actual, expected)

    def test_min_swaps_2(self):
        actual = minimum_swaps([2, 3, 4, 1, 5])
        expected = 3
        self.assertEqual(actual, expected)


    def test_min_swaps_3(self):
        actual = minimum_swaps([1, 2, 3, 4, 5])
        expected = 0
        self.assertEqual(actual, expected)

    def test_min_swaps_4(self):
        actual = minimum_swaps([1, 2, 3, 5, 4])
        expected = 1
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)