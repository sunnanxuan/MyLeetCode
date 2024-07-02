class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        stack = []
        i = 0
        while i < len(dominoes):
            if dominoes[i] == 'R' or dominoes[i] == 'L':
                stack.append(dominoes[i])
                i += 1
            elif dominoes[i] == '.':
                j = i + 1
                while j < len(dominoes) and dominoes[j] == '.':
                    j += 1
                if j == len(dominoes) or dominoes[j] == 'R':
                    if stack and stack[-1] == 'R':
                        stack.extend(['R'] * (j - i))
                    else:
                        stack.extend(['.'] * (j - i))
                elif dominoes[j] == 'L':
                    if stack and stack[-1] == 'R':
                        stack.extend(['R'] * ((j - i) // 2) + ['.'] * ((j - i) % 2) + ['L'] * ((j - i) // 2))
                    else:
                        stack.extend(['L'] * (j - i))
                i = j
        return ''.join(stack)

