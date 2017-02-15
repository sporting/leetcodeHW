# -*- coding: utf-8 -*-

#recursive 

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def find3sum(ns, res):
            # print ns
            if len(ns) < 3:
                return

            left = ns[0]
            right = ns[-1:][0]
            if (left > 0) or (right < 0):
                return

            middle = ns[1:-1]

            target = -1 * (left + right)

            if target in middle:
                result = [left, target, right]
                if result not in res:
                    res.append(result)
                    #print result
            
            if (left >= target >= right):
                return 

            rightnums = list(middle)
            rightnums.append(right)
            #print 'rightnums',str(rightnums)
            find3sum(rightnums, res)

            leftnums = list(middle)
            leftnums.insert(0, left)
            #print 'leftnums',str(leftnums)
            find3sum(leftnums, res)

        result = []
        #newnums = list(set(nums))
        nums.sort()
        print nums
        
        find3sum(nums, result)

        return result

if __name__ == "__main__":
    nums = [2,0,-3,-2,3,-1,-3,0,1,0,3,4,-5,2]
    solution = Solution()
    print solution.threeSum(nums)
