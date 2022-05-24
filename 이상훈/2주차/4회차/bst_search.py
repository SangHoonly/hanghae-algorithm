# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    VALUE = None
    found_node = None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search_bst(node):
            if not node:
                return

            cur_val = node.val

            if cur_val == self.VALUE:
                self.found_node = node
                return

            if cur_val < self.VALUE:
                search_bst(node.right)

            elif cur_val > self.VALUE:
                search_bst(node.left)

            return


        self.VALUE = val
        search_bst(root)


        return self.found_node
