# 분할 정복
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]


input_str = [2, 2, 1, 1, 1, 2, 2]
sol = Solution()
chk = sol.majorityElement(input_str)
print(chk)