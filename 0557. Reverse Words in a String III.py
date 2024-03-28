class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        s = s.split(' ')
        for c in s:
            stack.append(c[::-1])
        return ' '.join(stack)
