class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

    

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
# Example usage:
root = TreeNode(10)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.right = TreeNode(15)
root.right.left = TreeNode(14)
root.right.right = TreeNode(19)
root.right.right.right = TreeNode(20)

inverted_root = Solution().invertTree(root)
print(inverted_root)  # Output the root of the inverted tree
