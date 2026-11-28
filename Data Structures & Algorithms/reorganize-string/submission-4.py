class Solution:
    def reorganizeString(self, s: str) -> str:

        last = None
        res = []

        heap = [(-cnt, char) for char, cnt in Counter(s).items()]
        heapq.heapify(heap)

        while heap:
            cnt, char = heapq.heappop(heap)

            if char == last:
                if not heap:
                    return ""

                cnt2, char2 = heapq.heappop(heap)
                heapq.heappush(heap, (cnt, char))

                cnt, char = cnt2, char2
            
            res.append(char)
            cnt+=1
            last = char

            if cnt < 0:
                heapq.heappush(heap, (cnt, char))

        return "".join(res)

        