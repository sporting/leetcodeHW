# -*- coding: utf-8 -*-

import re


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = {'(': ')', '[': ']', '{': '}'}
        pattern = '[\(\[\{\)\]\}]'
        collections = re.findall(pattern, s)
        stack = []
        while len(collections) > 0:
            c = collections.pop()
            if c in h.values():
                stack.append(c)
            elif (stack == []) or (h[c] != stack.pop()):
                return False

        return stack == []

if __name__ == "__main__":
    solution = Solution()
    s = '(){}[]'
    print solution.isValid(s)
