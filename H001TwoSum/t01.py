# -*- coding: utf-8 -*-


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lastidx = len(nums) - 1
        for idx, val in enumerate(nums):
            for nextidx in range(lastidx - idx):
                if val + nums[nextidx + idx + 1] == target:
                    return [idx, nextidx + idx + 1]

if __name__ == "__main__":
    nums = [1, 2, 4]
    target = 3
    solution = Solution()
    print solution.twoSum(nums, target)
