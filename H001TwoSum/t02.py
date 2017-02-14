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
            if map.has_key(complement) and idx != map.get(complement):
                return [idx, map.get(complement)]
                
if __name__ == "__main__":
    nums = [0, 5, 11, 5]
    target = 10
    solution = Solution()
    print solution.twoSum(nums, target)
