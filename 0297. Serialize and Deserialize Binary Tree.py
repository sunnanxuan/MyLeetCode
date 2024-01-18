# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        self.data = [str(root.val)]
        q = [root]
        while q:
            new = []
            for n in q:
                if n.left:
                    self.data.append(str(n.left.val))
                    new.append(n.left)
                else:
                    self.data.append('#')
                if n.right:
                    self.data.append(str(n.right.val))
                    new.append(n.right)
                else:
                    self.data.append('#')
            q = new
        self.data = ' '.join(self.data)
        return self.data

    def deserialize(self, data):
        data = data.split()
        if not data:
            root = None
        else:
            root = TreeNode(int(data[0]))
            q = [root]
            i = 1
            while q:
                new = []
                for n in q:
                    if data[i] == '#':
                        n.left = None
                    else:
                        n.left = TreeNode(int(data[i]))
                        new.append(n.left)
                    if data[i + 1] == '#':
                        n.right = None
                    else:
                        n.right = TreeNode(int(data[i + 1]))
                        new.append(n.right)
                    i += 2
                q = new

        return root