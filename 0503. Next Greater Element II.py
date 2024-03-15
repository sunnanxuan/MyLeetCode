class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        for n in nums[::-1]:
            while stack and stack[-1] <= n:
                stack.pop()
            stack.append(n)
        res = []
        for n in nums[::-1]:
            while stack and stack[-1] <= n:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(n)
        return res[::-1]

