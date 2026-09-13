class Solution:

    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1

        while l < r:
            # Width is (r - l), height is min of the two walls
            width = r - l
            current_height = min(heights[l], heights[r])
            current_area = width * current_height

            largest = max(largest, current_area)

            # Move the pointer of the shorter line inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return largest