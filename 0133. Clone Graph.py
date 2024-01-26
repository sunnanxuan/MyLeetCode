"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def clone(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            root = Node(node.val, [])
            visited[node] = root
            for n in node.neighbors:
                nxt = clone(n)
                root.neighbors.append(nxt)
            return root

        return clone(node)
