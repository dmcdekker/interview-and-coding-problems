
import unittest

# Given a list of words, print a tuple of (first-letter, word) for each word, in order.
def tuple_word(lst):
    for word in lst:
        print (word[0], word)

print tuple_word(['this', 'is', 'a', 'list']) 

class Test(unittest.TestCase):
    data = [
            (['this'], ('t', 'this'))
            ]    
         

    def test_tuple_word(self):
        for [test_lst, expected] in self.data:
            actual = tuple_word(test_lst)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()