class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def sm(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0:
                memo[(i, j)] = triangle[i][j]
            elif j == 0:
                memo[(i, j)] = triangle[i][j] + sm(i - 1, j)
            elif j == i:
                memo[(i, j)] = triangle[i][j] + sm(i - 1, j - 1)
            else:
                memo[(i, j)] = triangle[i][j] + min([sm(i - 1, j), sm(i - 1, j - 1)])
            return memo[(i, j)]

        n = len(triangle)
        return min([sm(n - 1, j) for j in range(n)])


Console
