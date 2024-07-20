class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sma = sum(aliceSizes)
        smb = sum(bobSizes)
        d = (sma - smb) // 2
        a = set(aliceSizes)
        b = set(bobSizes)
        for n in a:
            if n - d in b:
                return [n, n - d]
