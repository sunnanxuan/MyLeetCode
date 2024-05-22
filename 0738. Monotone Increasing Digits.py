class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        stack = []
        less = False
        for c in str(n):
            if less:
                stack.append('9')
            else:
                if not stack or c >= stack[-1]:
                    stack.append(c)
                else:
                    arr = []

                    while stack and c < stack[-1]:
                        arr.append(c)
                        c = stack.pop()
                        c = str(int(c) - 1)
                    less = True
                    stack.append(c)
                    while arr:
                        stack.append('9')
                        arr.pop()
        return int(''.join(stack))

