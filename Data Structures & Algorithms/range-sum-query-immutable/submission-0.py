class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total+=n
            self.prefix.append(total)
        print(self.prefix)
    def sumRange(self, left: int, right: int) -> int:

        right_chunk = self.prefix[right]
        left_chunk = self.prefix[left-1] if left > 0 else 0
        print(f'Right sum for right={right}: {right_chunk}, Left sum for left={left}: {left_chunk}')
        return right_chunk - left_chunk 
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)