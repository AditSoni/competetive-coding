class Solution:
    def canJump(self, nums: List[int]) -> bool:

        score_array = [0] * len(nums)
        if 0 not in nums:
            return True
        # now here we try to reach end.
        len_num = len(nums)
        for i in range(len_num-1,0,-1):
            if ((i-1) + nums[i-1]) >= (len_num-1):
                score_array[i-1] = 1
                continue
            if nums[i-1] == 0:
                score_array[i-1] = 10000
                continue
            score_array[i-1] = min(score_array[i:i+nums[i-1]]) + 1
        
        
        return score_array[0] < 10000

            
