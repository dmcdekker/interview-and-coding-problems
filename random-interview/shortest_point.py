import unittest

    
def shortest_point(matrix):
    found_row = []
    found_col = []
    for row_num, row in enumerate(matrix):
        for col_num, element in enumerate(row):
            if element == 1:
                found_row.append(row_num)
                found_col.append(col_num)

    # print(found_row)
    # print(found_col)

    first_coord = abs(found_row[1] - found_row[0])
    second_coord = abs(found_col[1] - found_col[0])
    
    return max(first_coord, second_coord)


class Test(unittest.TestCase):

    def test_shortest_1(self):
        actual = shortest_point([[0, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0]])
        expected = 1 
        self.assertEqual(actual, expected)

    def test_shortest_2(self):
        actual = shortest_point([[0, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [0, 0, 0, 0, 1],
                                 [0, 0, 0, 0, 0]])
        expected = 3 
        self.assertEqual(actual, expected)

    def test_shortest_3(self):
        actual = shortest_point([[0, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 1, 0]])
        expected = 2 
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)