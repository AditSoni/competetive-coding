from typing import List


def group_anagrams(strs:List[str]) -> List[List[str]]:
    
    indexed_list = list(enumerate(strs))

    # sorting each element
    sorted_list = []
    for i in indexed_list:
        index,element = i
        sorted_list.append((index,sorted(element)))

    checked_index = set()
    ans = []
    for i in sorted_list:
        outer_index,list_ = i
        local_ans = [indexed_list[outer_index][1]]
        if outer_index in checked_index:
            continue
        checked_index.add(outer_index)
        for j in range(outer_index+1,len(strs)):
            if j in checked_index:
                continue
            inner_index , element = sorted_list[j]
            if list_ == element:
                checked_index.add(inner_index)
                local_ans.append(indexed_list[inner_index][1])
        ans.append(local_ans)

    return ans

def group_anamgrams1(strs):

    dict_s = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if dict_s.get(sorted_s):
            dict_s[sorted_s].append(s)
        else:
            dict_s[sorted_s] = [s]
    return list(dict_s.values())


list_of_str = ['cat','tac','bat','tab','','1','abc']
print(group_anamgrams1(list_of_str))