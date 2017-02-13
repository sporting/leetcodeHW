# -*- coding: utf-8 -*-

# take x be integer to mod

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)
        l = []
        while True:
            m = x % 10
            x = x / 10
            l.append(m)
            if x == 0:
                break

        digits = len(l)
        rv = 0
        for d in l:
            digits = digits -1
            rv = rv + 10**digits * d
        
        rv = rv * (-1 if negative else 1)

        return 0 if rv>=pow(2,31) or rv<pow(2,31)*(-1) else rv
        
        
if __name__ == '__main__':
    x = 555222255
    solution = Solution()
    print solution.reverse(x)
