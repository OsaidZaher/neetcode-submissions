class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) 
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        return stones[0]*-1 if stones else 0
        