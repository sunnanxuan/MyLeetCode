class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        stack_l = []
        cur = height[0]
        for h in height:
            if h < cur:
                stack_l.append(h)
            elif h >= cur:
                while stack_l:
                    l = stack_l.pop()
                    res += (cur - l)
                cur = h
                stack_l.append(h)
        stack_r = []
        cur = height[-1]
        for h in height[::-1]:
            if h < cur:
                stack_r.append(h)
            elif h > cur:
                while stack_r:
                    r = stack_r.pop()
                    res += (cur - r)
                cur = h
                stack_r.append(h)
        return res