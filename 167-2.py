import bisect
from typing import List


# bisect 모듈 + 슬라이싱
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k + 1:], expected)
            if i < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2


numbers = [2, 7, 11, 15]
target = 9
sol = Solution()
check = sol.twoSum(numbers, target)
print(check)