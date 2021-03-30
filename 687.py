from idlelib.tree import TreeNode


class Solution:
    res: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return 0

            # 존재하지 않는 노드까지 dfs 재귀 탐색
            left = dfs(root.left)
            right = dfs(root.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if root.left and root.left.val == root.val:
                left += 1
            else:
                left = 0
            if root.right and root.right.val == root.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최대값이 결과
            self.res = max(self.res, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)
        dfs(root)
        return self.res


roots = [5, 4, 5, 1, 1, 5]
S = Solution()
cnt = S.longestUnivaluePath(roots)
print(cnt)