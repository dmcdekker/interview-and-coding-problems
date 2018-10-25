import 

def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        new_arr = []
        while x:
            num = x % 10
            new_arr.append(int(num))
            x = (x - num) / 10

        return new_arr == new_arr[::-1]
