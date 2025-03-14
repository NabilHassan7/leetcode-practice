class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        pt1 = 0
        pt2 = len(numbers)-1
        while (pt2 > pt1):
            total = numbers[pt1] + numbers[pt2]
            if total == target:
                return [pt1+1,pt2+1]
            elif total > target:
                pt2 -= 1
            else:
                pt1 += 1
