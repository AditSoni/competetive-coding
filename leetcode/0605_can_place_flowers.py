from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        current_flower = 0
        if sum(flowerbed) == 0 :
            n -= flowers_count(len(flowerbed)+2)
        else:
            for i,item in enumerate(flowerbed):
                if not item:
                    current_flower += 1
                if item:
                    if current_flower == i:
                        current_flower +=1
                    
                    n -= flowers_count(current_flower)
                    current_flower = 0
            if current_flower:
                n -= flowers_count(current_flower+1)

        return n <= 0

def flowers_count(n):
    if n < 2 :
        return 0
    if n % 2 ==0:
        return (n//2) - 1 
    else:
        return n//2

print(canPlaceFlowers([0,0],1))
