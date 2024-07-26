"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {}

        def copylist(node):
            if not node: return None
            if node in visited:
                return visited[node]
            else:
                n = Node(node.val, None, None)
                visited[node] = n
                n.next = copylist(node.next)
                n.random = copylist(node.random)
                return n

        return copylist(head)
