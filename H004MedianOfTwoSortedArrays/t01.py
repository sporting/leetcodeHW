# -*- coding: utf-8 -*-


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        num = sorted(nums1 + nums2)
        medianpos = len(num) // 2
        if len(num) % 2 > 0:
            return num[medianpos]
        else:
            return (num[medianpos] + num[medianpos - 1]) / 2.0


if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2, 4]
    solution = Solution()
    print solution.findMedianSortedArrays(nums1, nums2)
