# -*- coding: utf-8 -*-

import math


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0:
            return False
        digitlen = int(math.log10(x)) + 1 

        for i in range(int(digitlen / 2.0) + 1):
            if i < 1:
                continue
            if i > (digitlen - i):
                break
            li = int(x / 10 ** (digitlen - i)) % 10
            ri = x % (10 ** i) / (10 ** (i - 1))

            if li != ri:
                return False

        return True

if __name__ == "__main__":
    x = 1234554321
    solution = Solution()
    print solution.isPalindrome(x)
