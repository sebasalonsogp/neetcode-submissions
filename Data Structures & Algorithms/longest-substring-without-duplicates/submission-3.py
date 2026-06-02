class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myChars = set()
        maxLen = 0
        l = 0 
        for r in range(len(s)):

            if s[r] in myChars:
                while s[r] in myChars:
                    myChars.remove(s[l])
                    l+=1

            myChars.add(s[r])
            maxLen = max(maxLen, len(myChars))        
        
        return maxLen
        