# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = []
        if root:
            self.travel(root)
        print(self.arr)
        self.i = -1

    def travel(self, node):
        if node.left:
            self.travel(node.left)
        self.arr.append(node.val)
        if node.right:
            self.travel(node.right)

    def next(self) -> int:
        if self.i < len(self.arr) - 1:
            self.i += 1
            self.cur = self.arr[self.i]
            return self.cur

    def hasNext(self):
        if self.i < len(self.arr) - 1:
            return True
        else:
            return False