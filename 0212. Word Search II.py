class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dic = {}
        for w in words:
            cur = dic
            for i in range(len(w)):
                if w[i] in cur:
                    cur = cur[w[i]]
                else:
                    cur[w[i]] = {}
                    cur = cur[w[i]]
            cur['#'] = '#'
        m = len(board)
        n = len(board[0])
        res = set()

        def search(i, j, used, cur, pre):
            if '#' in cur: res.add(pre)
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and (x, y) not in used and board[x][y] in cur:
                    search(x, y, used | {(x, y)}, cur[board[x][y]], pre + board[x][y])

        for i in range(m):
            for j in range(n):
                if board[i][j] in dic:
                    search(i, j, {(i, j)}, dic[board[i][j]], board[i][j])

        return list(res)
