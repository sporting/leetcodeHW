# -*- coding: utf-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        ziplist = zip(*strs)
        for tu in ziplist:
            char = ''
            for c in tu:
                if char == '':
                    char = c
                elif c != char:
                    return prefix
            prefix += char

        return prefix

if __name__=="__main__":
    solution = Solution()
    strs = ['abc','abcde','abceg','abcddd']
    print solution.longestCommonPrefix(strs)