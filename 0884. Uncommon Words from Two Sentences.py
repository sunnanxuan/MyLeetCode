class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1.split()+s2.split()
        dic=collections.Counter(s)
        return [k for k in dic if dic[k]==1]
