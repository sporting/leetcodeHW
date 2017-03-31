# -*- coding: utf-8 -*-

#O(n)2
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res=0
        for idx,n in enumerate(reversed(num1)):
            for idx2,n2 in enumerate(reversed(num2)):
                res = int(n)*int(n2)*10**idx2*10**idx+res
                
        return str(res)

if __name__ == "__main__":
    solution = Solution()
    num1 = "123"
    num2 = "456"
    print solution.multiply(num1,num2)