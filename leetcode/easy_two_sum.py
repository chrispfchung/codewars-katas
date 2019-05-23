class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make a loop to add first number to next to see if they match target
        #if it doesn't, move on to the next possible combo
        #when it does, return it
        #add nums[0] to nums[0+1+2++3+4]
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
