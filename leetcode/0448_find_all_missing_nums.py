from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums)+1)) - set(nums))
    


"""
iterate over the array : [4,3,2,7,8,2,3,1]
* for each item ; set the value of the value -1 index as negative , eg: set the 4th element value negative. (4-1) = 3rd index
* now array looks like [-4,-3,-2,-7,8,2,-3,-1]
* iterate over array and index where positve elements are present are the result
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        for i in range(len_):
            item = abs(nums[i])
            nums[item-1] = -abs(nums[item-1])

        return [i+1 for i in range(len_) if nums[i] > 0]