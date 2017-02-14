# -*- coding: utf-8 -*-
import math
# wiki: https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97

# 因數分解加上羅馬數字規則
# Factorization


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def checkNextDigit(v, r, ind, res):
            len = 10 ** int(math.log10(v - 1))
            if v > r >= (v - len):
                if (r / len == 9):
                    res.append(roman[ind + 2] + roman[ind])
                elif (r / len == 4):
                    res.append(roman[ind + 1] + roman[ind])
                r = r - (len * (r / len))
            return r, res

        romanint = [1000000, 500000, 100000, 50000,
                    10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
        roman = ['m', 'd', 'c', 'l', 'x', 'v',
                 'M', 'D', 'C', 'L', 'X', 'V', 'I']

        remainder = num
        result = []
        for idx, val in enumerate(romanint):
            s = remainder / val
            remainder = remainder % val
            if 4 > s > 0:
                result.append(roman[idx] * s)
                if val == 1:
                    break
                remainder, result = checkNextDigit(val, remainder, idx, result)
            elif s == 0:
                remainder, result = checkNextDigit(val, remainder, idx, result)

            if remainder == 0:
                break

        return ''.join(result)

if __name__ == '__main__':
    solution = Solution()
    # num = 65535
    # print solution.intToRoman(num)

    for i in xrange(88800, 88899):
        print '{:5d}:{}'.format(i, solution.intToRoman(i))
