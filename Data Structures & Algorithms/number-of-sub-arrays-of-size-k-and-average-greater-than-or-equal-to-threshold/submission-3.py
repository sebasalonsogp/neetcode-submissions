class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0 
        L = 0
        roll = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                roll -= arr[L]
                L+=1
            
            roll+= arr[R]

            if R - L + 1 == k and roll / k >= threshold:
                cnt+=1

        return cnt