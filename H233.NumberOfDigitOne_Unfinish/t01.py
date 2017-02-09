# -*- coding: utf-8 -*-

import math


class Solution(object):

    def countDigitOne2(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n / m + 8) / 10 * m + (n / m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        dig = len(str(abs(n)))
        if dig == 1:
            return 1 if n >= 1 else 0
        elif dig == 2:
            downdigs = int(str(n)[1:])
            headdig = int(str(n)[:1])
            if headdig > 1:
                return (headdig - 2) + 12 + self.countDigitOne(downdigs)
            else:
                return downdigs + 2 + self.countDigitOne(downdigs)
        elif dig > 2:
            downdigs = int(str(n)[1:])
            headdig = int(str(n)[:1])
            if headdig > 1:
                return headdig * math.pow(10, dig - 2)*2*(dig-2) + math.pow(10, dig - 1) + self.countDigitOne(downdigs)
            else:
                return headdig * math.pow(10, dig - 2)*2*(dig-2) + downdigs + self.countDigitOne(downdigs)

if __name__ == "__main__":
    nums = 1111
    solution = Solution()
    print 'Discuss solution: ' + str(solution.countDigitOne2(nums))
    print 'My solution: ' + str(solution.countDigitOne(nums))
