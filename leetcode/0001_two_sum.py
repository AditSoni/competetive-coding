def two_sum(num,target):
    map = {}
    results = []
    for i in range(len(num)):
        if num[i] not in map:     # store the key complement (sum - num) and value as current index 
            map[target - num[i]] = i  # when an item we need is in the dict ; we have found the pair ; we return the value at that key and the current index
        else:
            results.append((map[num[i]], i ))

    if not results:
        return -1, -1
    else :
        return results

print(two_sum([2,3,11,6,15,7],90))

