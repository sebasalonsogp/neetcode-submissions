class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxL = 0
        for n in nums:
            length = 1
            if n-1 not in numSet:
                while n+length in numSet:
                    length+=1
            maxL = max(maxL, length)

        return maxL