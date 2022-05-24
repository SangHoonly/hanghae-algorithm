from typing import Optional
from TreeNode import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def get_max_diameter(node) -> int:
            if not node:
                return 0

            left_max = get_max_diameter(node.left)
            right_max = get_max_diameter(node.right)

            return max(left_max, right_max) + 1

        def get_nodes(node, nodes):
            if not node:
                return

            nodes.append(node)

            get_nodes(node.left, nodes)
            get_nodes(node.right, nodes)


        ret = 0
        nodes = []

        get_nodes(root, nodes)

        for node in nodes:
            ret = max(ret, get_max_diameter(node.left) + get_max_diameter(node.right))


        return ret


