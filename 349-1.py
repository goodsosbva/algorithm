import bisect
from typing import List, Set


# 이진 검색으로 일치 여부 판별
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
sol = Solution()
check = sol.intersection(nums1, nums2)
print(check)