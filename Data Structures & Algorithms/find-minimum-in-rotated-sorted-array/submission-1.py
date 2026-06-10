class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # We know that if nums[mid] < nums[-1] we are in RIGHT sorted portion
        # We know that if nums[mid] > nums[-1] we are in LEFT sorted portion

        l,r =0 , len(nums)-1

        while l<r: # we need < not <= bc when l==r we are at our last candidate and it IS our answer.

            mid=(l+r)//2

            if nums[mid] < nums[-1]: # right sorted portion, ans is here or to left
                r = mid
            elif nums[mid] > nums[-1]: #left sorted portion, ans is to right
                l = mid + 1
            
        
        return nums[l]