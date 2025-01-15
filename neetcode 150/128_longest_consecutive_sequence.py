class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_num = list(sorted(set(nums)))
        count = 1
        longest = 1
        for i in range(len(sorted_num)-1):
            if sorted_num[i+1] - sorted_num[i] == 1:
                count += 1
            else:
                if count > longest:
                    count, longest = longest, count
                count = 1
        
        if count > longest:
            count, longest = longest, count
        return longest
