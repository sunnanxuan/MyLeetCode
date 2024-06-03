class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permutation(i):
            if i<len(s):
                arr=permutation(i+1)
                if s[i].isdigit():cur=[s[i]]
                else:cur=[s[i].lower(),s[i].upper()]
                res=[]
                for c in cur:
                    for t in arr:
                        res.append(c+t)
                return res
            else:
                return ['']
        return permutation(0)