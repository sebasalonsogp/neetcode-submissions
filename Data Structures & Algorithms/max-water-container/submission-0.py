class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0

        def calcHeight(l,r):
            return (r-l) * min(heights[l],heights[r])
        
        l, r = 0 , len(heights) - 1

        while l<r:
            maxHeight = max(maxHeight, calcHeight(l,r))

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return maxHeight
        