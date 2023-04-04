"""Ques : Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how
much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9
"""
from typing import List

"""
Ans :
Here we want to find trapping water

=> left and right end there is no wall
=> at any point we store water is :
water[i]= min (max_left_height,max_right_height)-arr[i];

to store left height and right max height any given point we can use two array.

so space would be O(n) and time would be O(n)
"""


def trap(height: List[int]) -> int:
    n = len(height)
    right_arr = [None] * n
    right_arr[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        right_arr[i] = max(height[i], right_arr[i + 1])

    leftmax = height[0]
    ans = 0
    print(right_arr)
    for i in range(1, n - 1):
        if height[i] < leftmax and right_arr[i + 1] > height[i]:
            ans += min(leftmax, right_arr[i + 1]) - height[i]
        else:
            leftmax = height[i]
    return ans
