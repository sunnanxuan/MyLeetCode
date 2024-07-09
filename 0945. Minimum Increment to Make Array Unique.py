class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        nums_set = {i for i in range(mn, mx + 1)}
        miss = sorted(list(nums_set - set(nums)), reverse=True)
        dic = collections.Counter(nums)
        arr = []
        for k in dic:
            if dic[k] > 1:
                arr.extend([k] * (dic[k] - 1))
        arr.sort()
        res = 0
        pre = mx
        for m in arr:
            while miss and miss[-1] < m:
                miss.pop()
            if miss:
                cur = miss.pop()
            else:
                cur = pre + 1
                pre += 1
            res += (cur - m)
        return res
