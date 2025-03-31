class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = collections.Counter(arr1)
        res = []
        for n in arr2:
            if n in dic:
                res.extend([n] * dic[n])
                dic.pop(n)
        arr = sorted(list(dic.keys()))
        for n in arr:
            res.extend([n] * dic[n])
        return res
