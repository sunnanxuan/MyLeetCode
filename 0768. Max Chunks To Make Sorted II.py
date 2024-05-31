class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        new = sorted(arr)
        dic = collections.defaultdict(list)
        for i, c in enumerate(new):
            dic[c].append(i)
        res = 0
        l = 0
        r = dic[arr[0]].pop(0)
        while l < len(arr):
            if l < r:
                l += 1
                r = max(r, dic[arr[l]].pop(0))
            else:
                res += 1
                l += 1
                if l < len(arr): r = dic[arr[l]].pop(0)
        return res

