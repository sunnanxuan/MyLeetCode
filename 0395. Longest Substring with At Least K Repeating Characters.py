class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        memo={}
        dic=collections.defaultdict(int)
        res=0
        for i in range(len(s)):
            dic[s[i]]+=1
            memo[i]=dic.copy()
            if min(dic.values())>=k:
                res=max(res,i+1)
        for i in range(len(s)):
            cur=memo[i].copy()
            for j in range(i):
                cur[s[j]]-=1
                if cur[s[j]]==0:
                    cur.pop(s[j])
                if min(cur.values())>=k:
                    res=max(res,i-j)
        return res
