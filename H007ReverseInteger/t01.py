# -*- coding: utf-8 -*-

# take x be string to reverse

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        #sl = [c for c in str(abs(x))]
        #sl.reverse()
        #res = int(''.join(sl))*(-1 if negative else 1)
        s = str(abs(x))[::-1]
        res = int(s)*(-1 if negative else 1)
        return 0 if res>=pow(2,31) or res<pow(2,31)*(-1) else res        
        
        
if __name__ == '__main__':
    x = 123
    solution = Solution()
    print solution.reverse(x)
