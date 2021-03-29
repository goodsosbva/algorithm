from idlelib.tree import TreeNode


class Solution:
    longest: int = 0

    def diameterOfBinartTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest


root = [1, 2, 3, 4, 5]
k = Solution()
cnt = k.diameterOfBinartTree(root)
print(cnt)