class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prepopulate the list
        res = [1] * (len(nums))
        
        # Prefix pass, do iterate multiplying the
        # accumulated prefix by the item itself
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        # Potfix pass, same thing, in reverse order
        # with prefix numbers in place.
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res