import unittest

def array_manipulation(n, queries):
    # set up array to 5 cols with zeros
    my_array = [0] * (n+1)
    
    # change values in array with data in queries: store difference beween current
    # and previous elements
    for first, last, value in queries:
        # increment value minus 1 to align with 1-indexed array
        my_array[first - 1] += value

        # decrement value
        my_array[last] -= value

                    # 1   2  3   4   5  
    # 1, 2, 100  ->  100 100 0   0   0       
    # 2, 5, 100  ->  100 200 100 100 100    
    # 3, 4, 100  ->  100 200 200 200 100

                    # 1  2  3  4  5  6  7  8  9  10
    # 1, 5, 3    ->   3  3  3  3  3  0  0  0  0  0      
    # 4, 8, 7    ->   3  3  3  10 10 7  7  7  0  0 
    # 6, 9, 1    ->   3  3  3  10 10 8  8  8  8  0 

    max_val = 0  
    # keep track of accumulated sum from each iteration
    accumulated_sum = 0 
    # iterate through array, adding positive items to return largest element
    for item in my_array:
        accumulated_sum += item
        if accumulated_sum > max_val:
            max_val = accumulated_sum
    return max_val




class Test(unittest.TestCase):

    def test_array_manipulation_1(self):
        actual = array_manipulation(5, [[1, 2, 100], [2, 5, 100],[3, 4, 100]] )
        expected = 200
        self.assertEqual(actual, expected)

    def test_array_manipulation_2(self):
        actual = array_manipulation(10, [[1, 5, 3], [4, 8, 7],[6, 9, 1]] )
        expected = 10
        self.assertEqual(actual, expected)

    def test_array_manipulation_3(self):
        actual = array_manipulation(10, [[2, 6, 8], [3, 5, 7],[1, 8, 1], [5, 9, 15]] )
        expected = 31
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)