class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = 0
        l = 0
        while l < len(flowerbed):
            if flowerbed[l] == 0:
                r = l + 1
                while r < len(flowerbed) and flowerbed[r] == 0:
                    r += 1
                d = r - l
                if d % 2 == 0:
                    print(m, l, '&')
                    if l == 0 or r == len(flowerbed):
                        m += d // 2
                    else:
                        m += d // 2 - 1
                else:
                    if l == 0 and r == len(flowerbed):
                        m += d // 2 + 1
                    else:
                        m += d // 2
                l = r + 1

            else:
                l += 1
        return m >= n
