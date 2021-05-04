from typing import List


# 투 포인터
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1  # 리턴 값 +1


numbers = [2, 7, 11, 15]
target = 9
sol = Solution()
check = sol.twoSum(numbers, target)
print(check)