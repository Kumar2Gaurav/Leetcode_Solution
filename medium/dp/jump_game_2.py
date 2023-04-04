from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        res = 0
        l, r = 0, 0
        while r < goal:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
