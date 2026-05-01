class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for number in nums:
            # Is it a sequence starter?
            if (number - 1) not in nums_set:
                length = 0
                # Look for next ones until they cease
                while (number + length) in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest
                