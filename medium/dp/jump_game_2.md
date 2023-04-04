You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.


Input: nums = [2,3,0,1,4]
Output: 2

solution

1. Have to select maximum jump from window  for have to reach till last.
2. There are two pointer for left and right start from 0 index.
3. Left pointer used to track every index.
4. Right pointer used to select maximum value from window.
5. res count to minimum path.
6. done