# 파이썬 다운 방식
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


input_str = [2, 2, 1, 1, 1, 2, 2]
sol = Solution()
chk = sol.majorityElement(input_str)
print(chk)