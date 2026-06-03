class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freqT = {}
        for c in t:
            freqT[c] = 1 + freqT.get(c,0)

        need = len(freqT) #we need to have this many valid chars in our window
        have = 0
        minLen = float('inf')
        freqS = {}
        res = [0,len(t)]
        l=0
        for r in range(len(s)):

            if s[r] in freqT:
               
                freqS[s[r]] = 1 + freqS.get(s[r], 0)
                if freqS[s[r]] == freqT[s[r]]:
                    have+=1
            
            while have == need:
                if minLen > r - l + 1:
                    minLen = r - l + 1
                    res = [l, r]
                if s[l] in freqT:
                    freqS[s[l]] -= 1
                    if freqS[s[l]] < freqT[s[l]]:
                        have-=1
                l+=1
        l,r = res
        return s[l:r+1] if minLen != float('inf') else ""

        

            
