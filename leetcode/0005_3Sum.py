def three_sum(nums,tg_sum):
    nums.sort()
    triplets = []
    tg_sum = 0
    for i in range(len(nums)-2):

        right = len(nums)-1
        left = i + 1

        while left < right:
            c_sum = nums[i] + nums[left] + nums[right]

            if c_sum == tg_sum:
                triplets.append([nums[i],nums[left],nums[right]])
                right -=1
                left +=1
            elif c_sum < tg_sum:
                left+=1
            else:
                right -=1
    print(triplets)

three_sum([12,3,1,2,-6,5,-8,6],0)