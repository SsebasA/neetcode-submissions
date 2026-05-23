class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        left_max = 0
        right_max = 0
        
        water_area = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                area = left_max - height[left]
                if area > 0:
                    water_area += area
                left += 1
            elif left_max >= right_max:
                area = right_max - height[right]
                if area > 0:
                    water_area += area
                right -= 1
            

        return water_area

