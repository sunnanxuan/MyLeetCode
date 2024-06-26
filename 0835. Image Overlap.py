class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        arr1 = {(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1}
        arr2 = {(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1}
        res = 0
        for x in range(-1 * n + 1, n):
            for y in range(-1 * n + 1, n):
                new = set()
                for i, j in arr1:
                    new.add((i + x, j + y))
                res = max(res, len(new & arr2))
        return res
