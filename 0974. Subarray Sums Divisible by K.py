class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        dic = collections.defaultdict(int)
        sm = 0
        for n in nums:
            sm += n
            if sm % k == 0: res += 1
            if sm % k in dic: res += dic[sm % k]
            dic[sm % k] += 1
        return res
