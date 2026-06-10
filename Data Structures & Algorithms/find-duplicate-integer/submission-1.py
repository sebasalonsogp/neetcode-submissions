class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # FAST, SLOW pointers
        # Since for each n in nums, 1 <= n <= len(nums)
        # Each n points to another index, giving us essentially a graph / linked list
        # Thus, we can use fast and slow pointers to detect a cycle

        slow, fast =  nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # move twice 
            
            if slow == fast:
                # Cycle detect, break out of it
                break

        # Now that we have found where the cycle starts, to get the duplicated integer,
        # we start another slow pointer from the beginning and increment both until they intersect again

        slow2 = nums[0]

        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        
        return slow2