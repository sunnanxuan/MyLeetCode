class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        l = 0
        r = arr[0]
        while l < len(arr):
            if l < r:
                l += 1
                r = max(r, arr[l])
            else:
                res += 1
                l += 1
                if l < len(arr): r = arr[l]
        return res
