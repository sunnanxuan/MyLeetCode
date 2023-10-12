class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, n):
            if n >= len(word):
                return True
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in used and board[i][j] == word[n]:
                used.add((i, j))
                if any(dfs(x, y, n + 1) for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))):
                    return True
                else:
                    used.discard((i, j))
                    return False
            else:
                return False

        w = set(word)
        lst = [c for l in word for c in l]
        for c in w:
            if c not in lst:
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                used = set()
                if dfs(i, j, 0):
                    return True
        return False