class Solution:
    def maxArea(self, height: list[int]) -> int:
        pt1 = 0
        pt2 = len(height) - 1
        max_water = 0

        while pt1 < pt2:
            current_water = (pt2 - pt1) * min(height[pt1],height[pt2])
            max_water = max(max_water, current_water)
            
            if height[pt1] < height[pt2]:
                pt1 += 1
            else:
                pt2 -= 1
        
        return max_water
