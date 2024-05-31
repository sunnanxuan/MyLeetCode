class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = collections.Counter(stones)
        res = 0
        for c in jewels:
            if c in dic: res += dic[c]
        return res
