class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        calc = {}
        # we know that for a given n, we want to find a target - n
        for i, n in enumerate(nums):
            x = target - n
            if n in calc.keys():
                return [calc[n], i]
            else:
                calc[x] = i