# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):


        queue = deque([(root, 0)])
        visited = []


        while queue:
            node, node_id = queue.popleft()

            if not node: continue

            cur_id, left_id, right_id = node_id, None, None

            if node.left:
                node_id += 1
                left_id = node_id
                queue.append((node.left, left_id))

            if node.right:
                node_id += 1
                right_id = node_id
                queue.append((node.right, right_id))


            visited.append(str({
                'node_id': str(cur_id),
                'val' : str(node.val),
                'left_id' : str(left_id),
                'right_id' : str(right_id)
            }))

        return '+'.join(visited)




    def deserialize(self, datas):
        if not datas:
            return None

        data_queue = deque(map(eval, datas.split('+')))
        root = TreeNode()

        node_queue = deque([root])
        while node_queue:
            node = node_queue.popleft()
            data = data_queue.popleft()
            node.val = int(data['val'])


            left, right = None, None

            if eval(data['left_id']):
                left = TreeNode()
                node_queue.append(left)

            if eval(data['right_id']):
                right = TreeNode()
                node_queue.append(right)

            node.left = left
            node.right = right

        print(root.val)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
