class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort()
        res=0
        for c in s:
            if g and c>=g[-1]:
                res+=1
                g.pop()
        return res
