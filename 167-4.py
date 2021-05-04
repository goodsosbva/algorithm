import bisect
from typing import List


# bisect 모듈 + 슬라이싱 제거
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1


numbers = [2, 7, 11, 15]
target = 9
sol = Solution()
check = sol.twoSum(numbers, target)
print(check)