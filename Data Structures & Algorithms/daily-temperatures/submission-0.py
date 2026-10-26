class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                j, popped_val = stack.pop()
                res[j] = i - j
            stack.append((i, val))

        return res