class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col=columnTitle[::-1]
        res=0
        for i,c in enumerate(col):
            res+=(ord(c)-64)*pow(26,i)
        return res