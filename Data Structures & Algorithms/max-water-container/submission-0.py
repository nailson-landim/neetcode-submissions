class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        L, R = 0, len(heights) - 1
        while L < R:
            current_volume = min(heights[L], heights[R]) * (R - L)
            if current_volume > max_volume:
                max_volume = current_volume
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return max_volume