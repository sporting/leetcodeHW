# -*- coding: utf-8 -*-


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for idx, val in enumerate(nums):
            map[val] = idx
            
        for idx, val in enumerate(nums):
            complement = target - val
            if map.has_key(complement):
                return [idx, map.get(complement)]

if __name__ == "__main__":
    nums = [1, 2, 4]
    target = 5
    solution = Solution()
    print solution.twoSum(nums, target)
