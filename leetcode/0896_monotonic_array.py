from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_decreasing = True
        is_increasing = True

        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                is_increasing = False
            if nums[i-1] < nums[i]:
                is_decreasing = False
            
        return is_increasing or is_decreasing

