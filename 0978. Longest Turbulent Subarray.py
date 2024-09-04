class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        pre = None
        res = 1
        l = 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                res = max(res, i - l + 1)
                l = i + 1
                pre = None
            else:
                if pre != None and pre == (arr[i] > arr[i + 1]):
                    res = max(res, i - l + 1)
                    l = i
                pre = (arr[i] > arr[i + 1])
        res = max(res, len(arr) - l)
        return res

