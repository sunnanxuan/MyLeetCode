class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def match(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s):
                if j == len(p):
                    memo[(i, j)] = True
                    return True

                elif p[j] == '*' or (j < len(p) - 1 and p[j + 1] == '*'):
                    memo[(i, j)] = match(i, j + 1)
                    return memo[(i, j)]
                elif p[j] != '*':
                    memo[(i, j)] = False
                    return False
            elif j == len(p):
                memo[(i, j)] = False
                return False

            if p[j] == '*':
                if p[j - 1] == s[i] or p[j - 1] == '.':
                    memo[(i, j)] = match(i + 1, j) or match(i + 1, j + 1) or match(i, j + 1)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = match(i, j + 1)
                    return memo[(i, j)]
            elif s[i] == p[j] or p[j] == '.':
                if j < len(p) - 1 and p[j + 1] == '*':
                    memo[(i, j)] = match(i + 1, j + 1) or match(i, j + 1)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = match(i + 1, j + 1)
                    return memo[(i, j)]
            elif s[i] != p[j]:
                if j < len(p) - 1 and p[j + 1] == '*':
                    memo[(i, j)] = match(i, j + 1)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = False
                    return False

        return match(0, 0)
