class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n)[2:][::-1]
        n+='0'*(32-len(n))
        return int(n,2)
