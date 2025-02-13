def move_ele(arr,ele):
    l = 0
    r = len(arr) - 1

    while l<r:
        curr_item = arr[l]
        while arr[r] == ele and l<r:
            r-=1

        if curr_item == ele:
            arr[r], arr[l] = arr[l],arr[r]
        l+=1
    
    return arr

print(move_ele([2,2,1,2222,2,2],2))
