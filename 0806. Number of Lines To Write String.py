class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        n=1
        l=0
        alp=string.ascii_lowercase
        dic={}
        for i in range(26):
            dic[alp[i]]=widths[i]
        for c in s:
            if l+dic[c]>100:
                n+=1
                l=0
            l+=dic[c]
        return [n,l]