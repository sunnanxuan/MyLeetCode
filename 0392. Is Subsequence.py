class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dic_t=collections.defaultdict(list)
        for i,c in enumerate(t):
            dic_t[c].append(i)
        cur=0
        for i ,c in enumerate(s):
            if not dic_t[c] or dic_t[c][-1]<cur:
                return False
            else:
                p=dic_t[c].pop(0)
                while p<cur:
                    p=dic_t[c].pop(0)
                cur=p
        return True