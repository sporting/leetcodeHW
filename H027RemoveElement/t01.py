# -*- coding: utf-8 -*-

# Time complexity is O(n)2
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in xrange(0,nums.count(val)):
            nums.remove(val)
            
        return len(nums)

if __name__=="__main__":
    solution = Solution()
    nums = [1,2,2,2,3,4,5]
    remove_num = 2
    print(solution.removeElement(nums, remove_num))