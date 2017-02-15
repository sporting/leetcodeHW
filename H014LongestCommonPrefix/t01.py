# -*- coding: utf-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        for i in xrange(65535):
            c = ''
            for str in strs:            
                if len(str) > i:
                    if c == '':
                        c = str[i]
                    elif c != str[i]:
                        return prefix
                else:
                    return prefix
            prefix += c
        return prefix

if __name__=="__main__":
    solution = Solution()
    strs = ['abc','abcde','abceg','abcddd']
    print solution.longestCommonPrefix(strs)