class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sum_pairs = []
        nums.sort()
        
        for i in range(0,len(nums)):
            pt1 = i
            
            if pt1 > 0 and nums[pt1] == nums[pt1-1]:
                continue
            
            pt2 = i + 1
            pt3 = len(nums) - 1
            
            while pt2 < pt3:
                total = nums[pt1] + nums[pt2] + nums[pt3]
            
                if total > 0:
                    pt3 -= 1
                elif total < 0:
                    pt2 += 1
                else:
                    sum_pairs.append([nums[pt1],nums[pt2],nums[pt3]])
                    pt2 += 1
                    
                    while (nums[pt2] == nums[pt2-1]) and pt2 < pt3:
                        pt2 += 1
        
        return sum_pairs
