class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        current_sum = None
        while current_sum != target:
            current_sum = numbers[L] + numbers[R]
            if current_sum == target:
                return [L + 1, R + 1]
            elif current_sum > target and R > 0:
                R -= 1
            elif current_sum < target and L < len(numbers) - 1:
                L += 1