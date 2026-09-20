class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        area = 0
        while l<r:
            height = min(heights[l],heights[r])
            base = r-l
            area = max(area , height*base)

            if height == heights[l]:
                l+=1
            if height == heights[r]:
                r-=1
        return area