# -*- coding: utf-8 -*-
import sys
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.insert(0,-1*sys.maxint-1)
        for i in xrange(len(nums)-1):
            if nums[i]<target<=nums[i+1]:
                return i # i+1-1
            elif nums[i]==target:
                return i-1 

        return len(nums)-1

if __name__=="__main__":
    solution = Solution()
    nums = [-5,-3,-1,1,3,5,7,9,11,13,15]
    target = 4
    print(solution.searchInsert(nums,target))