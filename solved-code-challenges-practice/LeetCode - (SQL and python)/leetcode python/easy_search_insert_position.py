#https://leetcode.com/problems/search-insert-position/description/

#binary search algortihm

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)

        #sort values for binary search prepration
        nums = sorted(nums)
        #create left and right "anchors"
        left = 0
        right = len(nums) - 1
        #this is where dynamic binary search happens through constant cutting and re-evaluation of the list
        while left <= right:
            median = (left+right) // 2
            if nums[median] == target:
                return median
            elif nums[median] < target:
                left = median + 1
                print(left)
            elif nums[median] > target:
                right = median - 1
