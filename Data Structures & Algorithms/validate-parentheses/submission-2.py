class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        valMap = {')' : '(', '}':'{', ']':'['}

        for c in s:
            if c in valMap.keys():
                if left and valMap[c] == left[-1]:
                    left.pop()
                else:
                    return False
            else:
                left.append(c)
        
        return not left