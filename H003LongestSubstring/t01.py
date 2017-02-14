# -*- coding: utf-8 -*-

# if input string is too long, the runtime error 'maximum recursion depth exceeded in cmp' occurs

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        def findNotRepeatString(s):
            tmpary = []            
            for subs in s:
                if subs in tmpary:
                    if len(tmpary) > len(s[1:]):
                        return tmpary
                    tmp = findNotRepeatString(s[1:])
                    return tmp if len(tmp) > len(tmpary) else tmpary
                tmpary.append(subs)
            return tmpary
            
        longestString = findNotRepeatString(s)
        print ''.join(longestString)
        return len(longestString)
                

if __name__ == "__main__":
    s='abcabcbb'

    solution = Solution()
    answer = solution.lengthOfLongestSubstring(s)
    print answer
