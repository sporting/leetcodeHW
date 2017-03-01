# -*- coding: utf-8 -*-

import math

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
    	res = "1"
        for i in xrange(n-1):
            res = self.solve(res)
            print res
        return res

    def solve(self, n):
        n_str = n
        
        result, last_c, left, icnt = "", n_str[0], 0, 0
        while len(n_str) > left:
            if (last_c != n_str[left]):
                result = result+str(icnt)+last_c
                icnt = 1
            else:
                icnt += 1
            
            last_c = n_str[left]
            
            left += 1
            
        result = result + str(icnt)+last_c
        
        return result


if __name__ == "__main__":
    solution = Solution()
    #print solution.solve("1211")
    solution.countAndSay(6)
