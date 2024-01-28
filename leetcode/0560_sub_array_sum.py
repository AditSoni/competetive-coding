class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        map_sum = {0:1} 
        # If at any point current_sum (prefix_sum) - k equals zero
        # that means we got to count it.
        # instead of making another if condition to complicate it 
        # we are assuming it already exists and have made the count of 0 as 1
        # if there is no such sub array whose sum is k , 
        # we never would increment the count variable 
        current_sum = 0

        for item in nums:
            current_sum += item
            
            if current_sum - k in map_sum:
                count+= map_sum[current_sum-k]
                # visualize you already had this sum lets say 2 as the prefix sum
                # now if it occurs again (in form of current sum - k ) , then we can say there are total 
                # that number of ways to make a subarry to get sum k.
            if map_sum.get(current_sum):
                map_sum[current_sum] +=1
            else:
                map_sum[current_sum] = 1
            
        return count
