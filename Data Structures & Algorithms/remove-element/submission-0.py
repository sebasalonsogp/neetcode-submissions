class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        i=0
        n = len(nums)
        j=n-1

        while i < n :
            print(f'i={i}, j={j}, n={n}')
            if nums[i] == val:
                print(f'nums[i]={nums[i]}, nums[j]={nums[j]}')
                nums[i] = nums[j]
                j-=1
                n-=1
            else:
                k+=1
                i+=1
            print(nums)

        return k