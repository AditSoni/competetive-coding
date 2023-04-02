

def topKfrequent(array,k) -> list:
        dict_count = {}
        for item in array:
            if item in dict_count:
                dict_count[item] +=1
            else:
                dict_count[item] = 0
        sorted_elements = [k for k,v in sorted(dict_count.items(),key=lambda x:x[1],reverse=True)]
        return sorted_elements[:k]


print(topKfrequent([1,1,1,4,5,3,6,6],2))