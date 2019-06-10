#977. Squares of a Sorted Array
#https://leetcode.com/problems/squares-of-a-sorted-array/

#Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        new_list = map(lambda x: x**2, A)
        return sorted(new_list, reverse=False)
