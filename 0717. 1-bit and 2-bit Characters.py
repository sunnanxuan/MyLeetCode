class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if not bits or bits[-1]==1:return False
        if 1 not in bits:return True
        bits.reverse()
        l=0
        while l<len(bits) and bits[l]==0:
            l+=1
        r=l
        while r<len(bits) and bits[r]==1:
            r+=1
        z=l-(r-l)%2
        return z>0