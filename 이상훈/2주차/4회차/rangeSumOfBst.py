# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    LOW_BOUND = None
    HIGH_BOUND = None
    result = None


    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def bst_sum(node):

            if not node: return

            val = node.val

            if self.LOW_BOUND <= val <= self.HIGH_BOUND:
                self.result += val

            if val >= self.LOW_BOUND:
                bst_sum(node.left)

            if val <= self.HIGH_BOUND:
                bst_sum(node.right)

            return


        self.LOW_BOUND, self.HIGH_BOUND, self.result = low, high, 0

        bst_sum(root)

        return self.result

