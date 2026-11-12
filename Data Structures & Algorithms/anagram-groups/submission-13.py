class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        res = defaultdict(list) 

        for s in strs:
            sortedS = ''.join(sorted(s)) # cat -> act key
            res[sortedS].append(s) # key act:['act', 'cat']

        return list(res.values())

        