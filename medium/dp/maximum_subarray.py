# https://leetcode.com/problems/maximum-subarray/?envType=study-plan&id=dynamic-programming-i

"""
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.

 Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = nums[0]
        ans = nums[0]
        for i in nums[1:]:
            a = max(a + i, i)
            ans = max(a, ans)
        return ans
