from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
        print(res)

    return res


list_nums = [4, 1, 2, 1, 2]
check = singleNumber(list_nums)
print(check)

