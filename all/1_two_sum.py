class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for key, val in enumerate(nums):
            diff = target - val
            if diff in num_map:
                return num_map[diff],key
            num_map[val] = key
        return []
