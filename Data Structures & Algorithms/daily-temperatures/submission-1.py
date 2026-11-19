class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []
        for index, val in enumerate(temperatures):
            while stack and stack[-1][1]< val:
                sIndex, sVal = stack.pop()
                res[sIndex] = index - sIndex
            stack.append((index, val))

        return res
        