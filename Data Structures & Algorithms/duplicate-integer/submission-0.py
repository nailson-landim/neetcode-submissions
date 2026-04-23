class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Cast the list into a set and compare their lenghts
        if len(set(nums)) != len(nums):
            return True
        return False