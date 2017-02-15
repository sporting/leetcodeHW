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
            if len(set(tu)) > 1:
                break
            prefix += tu[0]

        return prefix

if __name__=="__main__":
    solution = Solution()
    strs = ['abc','abcde','abceg','abcddd']
    print solution.longestCommonPrefix(strs)