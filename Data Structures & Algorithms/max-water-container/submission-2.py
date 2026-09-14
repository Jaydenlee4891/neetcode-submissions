class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l,r = 0,len(heights)-1
        while l<r:
            base = r-l
            height = min(heights[l],heights[r])
            area = max(area , base*height)

            if height == heights[l]:
                l+=1
            else: 
                r -=1
        return area
