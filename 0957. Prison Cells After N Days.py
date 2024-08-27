class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        memo1 = {}
        memo2 = {}
        m = 0
        arr = copy.copy(cells)
        while tuple(arr) not in memo1:
            memo1[tuple(arr)] = m
            memo2[m] = arr
            new = [0] * 8
            for j in range(1, 7):
                if arr[j - 1] == arr[j + 1]:
                    new[j] = 1
            arr = new
            m += 1
            if m == n: return arr
        cir = m - memo1[tuple(arr)]
        n -= memo1[tuple(arr)]
        n %= cir
        n += memo1[tuple(arr)]
        return memo2[n]
