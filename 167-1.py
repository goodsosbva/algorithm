from typing import List


# 이진 검색
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            print(k, v)
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1


numbers = [2, 7, 11, 15]
target = 9
sol = Solution()
check = sol.twoSum(numbers, target)
print(check)
