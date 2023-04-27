from collections import Counter
from math import sqrt


def countSpecialNumbers1(self,N,arr):
        # get unique elements
        # get count of elements
        # get factors of numbers.
        
        unique = set(arr)
        count = 0 
        count_elements = Counter(arr)
        for i in unique:
            count_of_i = arr.count(i)
            count_elements[i] = count_of_i
            if count_of_i >1:
                count+=count_of_i
            else:
                for j in range(1,int(sqrt(i))+1):
                    if (i%j==0) and (j in unique):
                        count+=1
                
        return count

# geek for geeks solution

def countSpecialNumbers(N, arr):
        
        frequency = dict()

        maxVal = 0
        for i in arr:
            maxVal=max(i,maxVal)
            if(i in frequency):
                frequency[i]+=1
            else:
                frequency[i]=1
        
        specialNumbers = set()
        for i in frequency:
            for j in range(2*i,maxVal+1, i):
                if(j in frequency):
                    specialNumbers.add(j)
             
        ans = 0
        
        for ele in frequency.keys():
            if(frequency[ele]>1):
                ans+=frequency[ele]
            
            elif(ele in specialNumbers):
                ans+=1
        
        return ans

print(countSpecialNumbers(1,[2,2,2,2,2,3,3,3,3,3,9,11,18]))
# implementation breakdown
"""
Finding count of each element and all distinct elements

"""