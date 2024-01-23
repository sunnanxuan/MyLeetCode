class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack=preorder.split(',')
        null=0
        while stack:
            cur=stack.pop()
            if cur=='#':
                null+=1
            else:
                if null>=2:
                    stack.append('#')
                    null-=2
                else:
                    return False
        return not stack and null==1
