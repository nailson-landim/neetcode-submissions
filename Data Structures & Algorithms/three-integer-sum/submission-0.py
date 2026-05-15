class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        n = len(nums)
        for i in range(n - 2):
            # positive number doesn't sums zero in an ordered list
            if nums[i] > 0:
                break
            # skip the duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i + 1, n - 1
            while L < R:
                current_sum = nums[i] + nums[L] + nums[R]
                if current_sum < 0:
                    L += 1
                elif current_sum > 0:
                    R -= 1
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    # move left pointer as a way to avoid duplicates
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return result

            