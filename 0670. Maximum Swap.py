class Solution:
    def maximumSwap(self, num: int) -> int:
        s=str(num)
        lst=[c for c in s]
        lst.sort(reverse=True)
        for i in range(len(s)):
            if s[i]<lst[i]:
                p=s[::-1].index(lst[i])
                j=len(s)-1-p
                break
        else:return num
        l=s[i]
        r=s[j]
        s=s[:i]+r+s[i+1:j]+l+s[j+1:]
        return int(s)