def two_sum(num,target):
    map = {}
    for i in range(len(num)):
        if num[i] not in map:
            map[target - num[i]] = i
        else:
            return map[num[i]], i 

    return -1, -1

print(two_sum([2,3,11,6,15,7],9))