class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for c in asteroids:
            if not stack:stack.append(c)
            else:
                p=stack.pop()
                while stack and (p>0 and c<0) and abs(p)<abs(c):
                    p=stack.pop()
                if p>0 and c<0:
                    if abs(p)>abs(c):
                        stack.append(p)
                    elif abs(p)<abs(c):
                        stack.append(c)
                    elif abs(p)!=abs(c):
                        stack.append(p)
                        stack.append(c)
                else:
                    stack.append(p)
                    stack.append(c)
        return stack