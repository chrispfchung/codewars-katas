#https://leetcode.com/problems/search-insert-position/description/

#binary search algortihm

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #add target number if it isn't in given list
        if target not in nums:
            nums.append(target)
        #sort values for binary search prepration
        nums = sorted(nums)
        #create left and right "anchors"
        left = 0
        right = len(nums) - 1

        #set median
        median = right // 2

        #create dynamic median loop
        while left <= right:
            if nums[median] == target:
                return median
            elif nums[median] < target:
                median = median + 1
            elif nums[median] > target:
                median = median - 1
