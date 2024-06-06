class Solution:
    def bestRotation(self, nums: List[int]) -> int:

        arr = [i - c for i, c in enumerate(nums)]
        m = sum([c >= 0 for c in arr])
        res = [m, 0]
        dic = collections.Counter(arr)
        n = len(nums)
        for k in range(n - 1):
            dic[arr[k]] -= 1
            dic[arr[k] + n] += 1
            if arr[k] < k and arr[k] + n >= k: m += 1
            m -= dic[k]
            if m > res[0]: res = [m, k + 1]
        return res[1]
