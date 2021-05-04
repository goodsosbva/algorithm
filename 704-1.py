
from typing import List

# 반복
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


numbers = [-1, 0, 3, 5, 9, 12]
target = 9
sol = Solution()
check = sol.search(numbers, target)
print(check)