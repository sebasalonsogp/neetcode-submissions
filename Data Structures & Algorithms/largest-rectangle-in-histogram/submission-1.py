class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Know that if height[i] < height[i-1], then height[-1] can no longer contribute any height going forward,
        # So we pop and calculate its area/histogram
        # We also know that for any height[i], its histogram isnt dependent on just its positon i
        # It could have a starter index at an earlier i, which allows its area to extend and this is the index we want
        # So anytime we actually do pop because we are at a smaller height, we should set that indexes start height
        # to the positon we popped since it extends backward

        maxArea = 0
        vals = [] # index, height

        for i, h in enumerate(heights):
            start = i # this could be our current start index
            while vals and h < vals[-1][1]: # if current height is smaller
                index, height = vals.pop()
                maxArea = max(maxArea, height * (i -  index)) # height * current index - starting index for that block
                start = index # since the current height is smaller, our current index can extend backwards
            
            vals.append([start, h])

        # But we are not done yet, because this first loop doesnt calculate maxArea with the remaining elements
        # in the stack where we did not find a subsequent smaller element to pop and calculate height. Thus,
        # We pop and calculate their area extending until the end. 

        while vals:
            index, height = vals.pop()
            maxArea = max(maxArea, height * (len(heights) -  index))

        return maxArea