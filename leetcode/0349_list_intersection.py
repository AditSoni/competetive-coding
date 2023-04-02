
def intersection(nums1, nums2):
    set_1 = set(nums1)
    set_2 = set(nums2)

    return set_1.intersection(set_2)

def intersection_2(nums1,nums2):
    res = set()
    item_dict = {}

    for item in nums1:
        if item not in item_dict:
            item_dict[item] = 1
    
    for item in nums2:
        if item in item_dict:
            res.add(item)

    return res
