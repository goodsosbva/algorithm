from typing import List, Set


# 브루트 포스 계산
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)

        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
sol = Solution()
check = sol.intersection(nums1, nums2)
print(check)