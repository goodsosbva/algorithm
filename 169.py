from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num


input_str = [2, 2, 1, 1, 1, 2, 2]
sol = Solution()
chk = sol.majorityElement(input_str)
print(chk)