class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        dic=collections.Counter(strs)
        strs=sorted(list(set(strs)),key=lambda x:-1*len(x))
        def subsequence(s,t):
            p=0
            for c in t:
                if c==s[p]:
                    p+=1
                    if p==len(s):return False
            return True
        for i in range(len(strs)):
            if dic[strs[i]]>1:
                continue
            if i==0:
                return len(strs[i])
            if all([subsequence(strs[i],strs[j]) for j in range(i)]):
                return len(strs[i])
        return -1