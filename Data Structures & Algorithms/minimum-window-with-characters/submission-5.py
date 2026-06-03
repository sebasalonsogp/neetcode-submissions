class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freqT = {}
        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)

        freqS = {}
        need = len(freqT)
        have = 0

        res = [-1, -1]
        minLen = float("inf")
        l = 0

        for r, char in enumerate(s):
            if char in freqT:
                freqS[char] = 1 + freqS.get(char, 0)

                if freqS[char] == freqT[char]:
                    have += 1

            while have == need:
                windowLen = r - l + 1

                if windowLen < minLen:
                    minLen = windowLen
                    res = [l, r]

                leftChar = s[l]

                if leftChar in freqT:
                    freqS[leftChar] -= 1

                    if freqS[leftChar] < freqT[leftChar]:
                        have -= 1

                l += 1

        left, right = res
        return "" if minLen == float("inf") else s[left:right + 1]