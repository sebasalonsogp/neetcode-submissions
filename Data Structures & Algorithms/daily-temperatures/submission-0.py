class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        stack = []

        for i, curTemp in enumerate(temperatures):

            while stack  and temperatures[stack[-1]] < curTemp:
                prev = stack.pop()
                res[prev] = i - prev # days since new temp and cur temp

            stack.append(i)

        return res
