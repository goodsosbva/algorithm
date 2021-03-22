from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(csum, index, path):
        # 종료조건
        if csum < 0:
            return
        if csum == 0:
            res.append(path)
            return

        # 자신 부터 하위 원소 까지의 나열 재귀 호출

        for i in range(index, len(candidates)):
            print(csum - candidates[i], i, path + [candidates[i]])
            dfs(csum - candidates[i], i, path + [candidates[i]])


    dfs(target, 0, [])
    return res


ans = combinationSum([2, 3, 6, 7], 7)
print(ans)