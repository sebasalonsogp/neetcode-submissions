class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        l,r= 0,0
        mostFreq = 0
        maxWindow = 0
        while r < len(s):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            mostFreq = max(mostFreq, freqs[s[r]])
            while (r - l + 1) - mostFreq > k:  #while window is NOT valid
                freqs[s[l]] -= 1
                l+=1
            maxWindow = max(maxWindow, r-l+1)
            r+=1

        return maxWindow
