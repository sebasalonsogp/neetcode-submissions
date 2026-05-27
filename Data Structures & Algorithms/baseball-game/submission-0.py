class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = []
        for i, op in enumerate(operations):
            if op == '+':
                res.append(res[-1]+res[-2])
            elif op =='D':
                res.append(2 * res[-1])
            elif op == 'C':
                res.pop()
            else:
                res.append(int(op))


        return sum(res)
