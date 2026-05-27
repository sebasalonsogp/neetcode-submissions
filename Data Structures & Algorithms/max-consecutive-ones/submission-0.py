class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, lst = 0 , 0
        tot = 0
        for n in nums:
            lst = n
            if lst == 1:
                cnt+=1
            else:
                cnt=0
            if tot < cnt:
                tot = cnt
        return tot
        