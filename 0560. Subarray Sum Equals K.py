class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(int)
        count[0] = 1
        sm = 0
        res = 0
        for n in nums:
            sm += n
            if sm - k in count:
                res += count[sm - k]
            count[sm] += 1
        return res
