class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        c = image[sr][sc]
        m = len(image)
        n = len(image[0])

        def change(i, j):
            image[i][j] = color
            visited.add((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and image[x][y] == c:
                    change(x, y)

        change(sr, sc)
        return image
