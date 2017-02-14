# -*- coding: utf-8 -*-
import math
# wiki: https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'m': 1000000, 'd': 500000, 'c': 100000, 'l': 50000, 'x': 10000,
                 'v': 5000, 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        group = [['m', 'c'], ['d', 'c'], ['c', 'x'], ['l', 'x'], ['x', 'M'], ['v', 'M'], [
            'M', 'C'], ['D', 'C'], ['C', 'X'], ['L', 'X'], ['X', 'I'], ['V', 'I']]
        sl = len(s)
        num = 0
        lastc = ''
        for i in xrange(sl):
            c = s[sl - i - 1]
            if (c in ['I', 'X', 'C', 'M', 'x', 'c', 'm']) and ([lastc, c] in group):
                num -= roman.get(c)
            else:
                num += roman.get(c)

            lastc = c
        return num


if __name__ == '__main__':
    solution = Solution()
    s = 'XLIX'
    print solution.romanToInt(s)
