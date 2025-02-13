def sum_dff(arr1,arr2):
    arr1.sort()
    arr2.sort()

    p1 = p2 = 0

    smallest_diff = float('inf')
    current_diff = float('inf')
    res = ()
    while p1<len(arr1) and p2<len(arr2):
        first_element = arr1[p1]
        second_element = arr2[p2]

        if first_element < second_element:
            current_diff = second_element - first_element
            p1+=1
        elif first_element > second_element:
            current_diff = first_element - second_element
            p2+=1
        else:
            return first_element,second_element
        
        if smallest_diff > current_diff:
            smallest_diff = current_diff
            res = first_element,second_element

    return res

print(sum_dff([1,22,23,12,44,52],[224,22225,122,121,100,424]))