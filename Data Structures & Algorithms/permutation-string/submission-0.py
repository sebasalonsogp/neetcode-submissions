class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        # First create a frequency map for our chars 
        freqMap = {}
        for s in s1:
            freqMap[s] = freqMap.get(s, 0) + 1

        k = len(s1) # Window size
        
        countMap = {}

        l, r = 0, 0
        while r < len(s2):
            countMap[s2[r]] = 1 + countMap.get(s2[r],0)
            
            # Fix window size
            while r - l + 1 > k:
                countMap[s2[l]] -= 1
                if countMap[s2[l]] == 0:
                    del countMap[s2[l]]
                l+=1

            # If our window was able to extend to size len(s1), then we must have found a perm.
            if countMap.items() == freqMap.items():
                return True

            r+=1
        
        # Otherwise, there were no valid permutations found
        return False