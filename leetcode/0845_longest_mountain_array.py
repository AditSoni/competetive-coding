class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest_peak = 0
        i = 1

        while i < len(arr)-1:
            
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                # left
                left = 1
                j = i -1 
                while j > 0:
                    if arr[j] > arr[j-1]:
                        left+=1
                        j-=1
                    else:
                        break

                right = 1
                k = i+1
                # right
                while k < len(arr)-1:
                    if arr[k] > arr[k+1]:
                        right+=1
                        k+=1
                    else:
                        break
                
                peak = left + right + 1
                longest_peak = peak if peak > longest_peak else longest_peak

                i = k+1
                continue
            i+=1

        return longest_peak
    


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest_peak = 0
        i = 1

        while i < len(arr)-1:
            is_peak = arr[i] > arr[i-1] and arr[i] > arr[i+1]
            if not is_peak:
                i+=1
                continue
            
            left = i -2
            while left >= 0 and arr[left] < arr[left+1]:
                left -=1
            
            right = i+2
            while right < len(arr) and arr[right] < arr[right-1]:
                right+=1
            
            current_peak = right - left -1 
            longest_peak = max(current_peak,longest_peak)
            i = right

        return longest_peak