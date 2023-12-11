class Solution:
    def hammingWeight(self, n: int) -> int:
        n=bin(n)
        dic=collections.Counter(n)
        return dic['1']