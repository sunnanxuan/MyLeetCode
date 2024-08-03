# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = [(root, 0)]
        self.pre = None
        l = 1
        while True:
            new = []
            while self.q:
                node, s = self.q.pop()
                if node.left:
                    new.append((node.left, 0))
                else:
                    self.q.append((node, 0))
                    break
                if node.right:
                    new.append((node.right, 0))
                else:
                    self.q.append((node, 1))
                    break
            self.pre = self.q
            self.q = new

            if len(new) < 2 * l:
                break
            else:
                self.q.reverse()
            l *= 2

    def insert(self, val: int) -> int:
        node, s = self.pre.pop()
        if s == 0:
            self.pre.append((node, 1))
            node.left = TreeNode(val)
            self.q.append((node.left, 0))
        else:
            node.right = TreeNode(val)
            self.q.append((node.right, 0))
        if not self.pre:
            self.q.reverse()
            self.pre = self.q
            self.q = []
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()