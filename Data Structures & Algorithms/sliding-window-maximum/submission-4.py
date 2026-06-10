class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # We want to maintain a deque in descending order
        # if we a find a bigger num than top of deque, pop until descending order is maintain
        # We store indices this way we can easily check if particular num is no longer in our window thus we can popleft
        # Our result we add to the return array will simply be the leftmost node of the deque

        deque = collections.deque()
        res = []   
        l=0
        for i in range(len(nums)):

            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()

            deque.append(i)

            if deque[0] < l: 
                deque.popleft() # remove left element bc its out of bounds
            
            if i-l+ 1 >= k:
                res.append(nums[deque[0]]) # dont pop bc deque[0] could be answer for next iteration
                l+=1


        return res