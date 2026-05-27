class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        print(f'arr:{arr},k={k},threshold={threshold}')
        cnt = 0 
        window = []
        l=0
        roll = 0
        for r in range(len(arr)):
            # Add value to current window
            window.append(arr[r])
            #print(f'Current window: {window} with Sum {sum(window)} and Average {sum(window)/k}')
           

            # If window is too large, remove first from window and current rolling average
            if r - l + 1> k:
                window.pop(0)
                l+=1
             # Check if current window avg meets threshold requirement
            if len(window)==k and sum(window) / k >= threshold:
                cnt+=1
            
        return cnt