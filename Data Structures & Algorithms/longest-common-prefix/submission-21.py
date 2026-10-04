'''
have 2 pointers one at word and another at word 1 

if two pointers are equal res = pointer
continue while they are equal when it breaks pointer 0 +=1 poitner 1+=1
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(len(strs)):
            j = 0
            while j< min(len(prefix), len(strs[i])):
                if prefix[j]!= strs[i][j]:
                    break
                j+=1
            prefix = prefix[:j]
        return prefix



        