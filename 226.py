from idlelib.tree import TreeNode


def invertTree(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = \
            invertTree(root.right), invertTree(root.left)
        return root
    return None
