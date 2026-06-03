class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        for i, n in enumerate(nums):
            l=i+1
            r=len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                    while nums[r] == nums[r+1] and l < r:
                        r-=1
                
        return res
