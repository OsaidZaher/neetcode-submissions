'''

- there are n people in the town all labelled from 1-n
- there may be a judge
- if judge: judge trust nobody, everybody trusts the town judge, one person satisifes 1 and 2
- given an array trust- [ai, bi] where ai trusts bi
return the label of the town judge if exists else -1

- given an array with tuple values,
- array[i] = [ai,bi] -> where ai  trusts bi
- return the bi value that is the trustee of all values but has nobody to trust

--

adj1 = { 3:[1,2], 1:[], 2:[]}
adj2 = {1:3, 4:3, 2:3, 3:[]}

we create two adj lists and we see if some key has both all value in adj1 and has no values in adj2

if one satisfies both of these requirements we can return it else return -1






'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trusts = defaultdict(int)
        trustedBy = defaultdict(int)

        for a, b in trust:
            trusts[a]+=1
            trustedBy[b]+=1

        for i in range(1, n+1):
            if trusts[i] == 0 and trustedBy[i] == n-1:
                return i

        return -1

