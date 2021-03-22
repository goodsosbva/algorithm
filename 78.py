from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(index, path):
        # 매번 결과 추가
        res.append(path)
        
        # 경로를 만들면서 DFS
        for i in range(index, len(nums)):
            print(path + [nums[i]])
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return res


setnums = subsets([1, 2, 3])
print(setnums)
