# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        res = [str(root.val)]
        q = [root]
        while q:
            new = []
            for node in q:
                if node.left:
                    new.append(node.left)
                    res.append(str(node.left.val))
                else:
                    res.append('#')
                if node.right:
                    new.append(node.right)
                    res.append(str(node.right.val))
                else:
                    res.append('#')
            q = new
        data = ','.join(res)
        return data

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            root = None
        else:
            data = data.split(',')
            data.reverse()
            c = data.pop()
            root = TreeNode(c)
            q = [root]
            while q:
                new = []
                for node in q:
                    l = data.pop()
                    r = data.pop()
                    if l == '#':
                        node.left = None
                    else:
                        node.left = TreeNode(int(l))
                        new.append(node.left)
                    if r == '#':
                        node.right = None
                    else:
                        node.right = TreeNode(int(r))
                        new.append(node.right)
                q = new
            return root

