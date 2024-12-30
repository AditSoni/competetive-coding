from typing import List
def missingNumber( nums: List[int]) -> int:
    length = len(nums)
    return int(length*(length+1)/2 - sum(nums))
