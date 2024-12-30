from typing import List

# def containsDuplicate(nums: List[int]) -> bool:
#         ordered = sorted(nums)
#         result = list(zip(ordered[:-1], ordered[1:]))
#         print(result)
#         for a, b in result:
#             if a == b:
#                 return True
#         return False 

# print(containsDuplicate([1,2,3,4,4,5,6]))


def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))