class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # The goal is to get the value that is either the timestamp or most recent to it
        # In otherwords, the max to the left of the timestamp
        
        target = self.store[key]

        l,r=0,len(target)-1
        res = ""
        while l<=r:

            mid =  (l+r) // 2

            if target[mid][1] <= timestamp: # Possible value found, move left pointer up
                res = target[mid][0]
                l=mid+1
            elif target[mid][1] > timestamp: # too large, shrink to left
                r=mid-1
            else:
                return res
            
        return res