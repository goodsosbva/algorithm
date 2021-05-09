from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))

        return r


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
sol = Solution()
chk = sol.maxSlidingWindow(nums, k)
print(chk)