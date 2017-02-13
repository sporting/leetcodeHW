# -*- coding: utf-8 -*-


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        cur, direct, rv = 0, False, {}
        for c in s:
            rv[cur] = (rv[cur] if rv.has_key(cur) else '') + c
            direct = not direct if (cur == 0) or (cur == numRows - 1) else direct
            cur = cur + 1 * (1 if direct else -1)

        return ''.join(rv.values())

if __name__ == '__main__':
    numRows = 5
    s = 'wkpacxzafxqkxsvmjqeadpbmvbtbupgsbysdvtecqwmqqiecaicdyervhkyebhwcfricmofdmttddxfehjhhnbdxnbbp'
    solution = Solution()
    print solution.convert(s, numRows)
