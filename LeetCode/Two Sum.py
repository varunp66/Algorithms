class Solution:
    def twoSum(self, nums, target):
        hashed = {}
        for i, n in enumerate(nums):
            if target-n in hashed: return [hashed[target-n], i]
            hashed[n] = i
