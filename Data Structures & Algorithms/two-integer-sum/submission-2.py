class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map each value to its original index before sorting
        indexed = sorted(enumerate(nums), key=lambda x: x[1])
        
        left, right = 0, len(indexed) - 1
        
        while left < right:
            current_sum = indexed[left][1] + indexed[right][1]
            if current_sum == target:
                i, j = indexed[left][0], indexed[right][0]
                return [min(i, j), max(i, j)]
            elif current_sum < target:
                left += 1
            else:
                right -= 1