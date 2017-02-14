# -*- coding: utf-8 -*-

# Time Limit Exceeded

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
                    return tmpary
                tmpary.append(subs)
            return tmpary
            
        substring = []
        while len(s) > 0:
            tmpstring = findNotRepeatString(s)
            if len(tmpstring) > len(substring):
                substring = tmpstring
            s=s[1:]

            if len(substring) > len(s):
                break

        print ''.join(substring)
        return len(substring)
                        

if __name__ == "__main__":
    s="abcabcbb"
    solution = Solution()
    answer = solution.lengthOfLongestSubstring(s)
    print answer


