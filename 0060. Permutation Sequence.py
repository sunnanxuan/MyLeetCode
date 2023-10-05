class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s=[str(i) for i in range(1,n+1)]
        p=list(itertools.permutations(s,n))[k-1]
        return "".join(list(p))