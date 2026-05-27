class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for word in strs:
            freq = [0] * 26 # 26 letters in alphabet
            for c in word:
                freq[ord(c)-ord('a')] += 1 # Make the letter 'a' equal = index 0 
            res[tuple(freq)].append(word)      

        
        return list(res.values())