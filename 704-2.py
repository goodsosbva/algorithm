import bisect
from typing import List

# 이진 검색 모듈
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


numbers = [-1, 0, 3, 5, 9, 12]
target = 9
sol = Solution()
check = sol.search(numbers, target)
print(check)