class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        print(freq)
        buckets = collections.defaultdict(list) # bucket from 1->n
        
        for key, v in freq.items():
            buckets[v].append(key)
        print(buckets)

        n = len(nums)
        while n >= 0:
            if len(res) == k:
                return res
            while buckets[n]:
                res.append(buckets[n].pop())
                if len(res) == k:
                    return res

            n-=1
        return res