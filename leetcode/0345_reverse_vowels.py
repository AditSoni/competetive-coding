def reverseVowels(s: str) -> str:
        s_list = list(s)
        if ('a' not in s) and ('e' not in s) and ('i' not in s) and ('o' not in s) and ('u' not in s) and ('A' not in s) and ('E' not in s) and ('I' not in s) and ('O' not in s) and ('U' not in s):
            return s
        vowels = 'aeiouAEIOU'
        vowel_list = []
        for i,item in enumerate(s):
            if item in vowels:
                vowel_list.append((i,item))

        vowel_length = len(vowel_list)
        for i in range(vowel_length//2):
            index1,value1 = vowel_list[i]
            index2,value2 = vowel_list[vowel_length-i-1]

            s_list[index1],s_list[index2] = value2,value1
        
        return ''.join(s_list)


def reverseVowels_pointer(s: str) -> str:
        s_list = list(s)
        vowels = 'aeiouAEIOU'

        i = 0
        j = len(s_list) - 1 

        while (i < j ):
            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i],s_list[j] = s_list[j],s_list[i]
                i+=1
                j-=1
            elif s_list[i] in vowels:
                j-=1
            elif s_list[j] in vowels:
                i+=1
            else:
                i+=1
                j-=1
            
        
        return ''.join(s_list)

print(reverseVowels_pointer('hello'))