from idlelib.tree import TreeNode


class Solution:
    result = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return None

            left = dfs(root.left)
            right = dfs(root.right)

            if root.left and root.val == root.left.val:
                left += 1
            else:
                left = 0
            if root.right and root.val == root.right.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)
        dfs(root)
        return self.result

roots = [5, 4, 5, 1, 1, 5]
S = Solution()
cnt = S.longestUnivaluePath(roots)
print(cnt)