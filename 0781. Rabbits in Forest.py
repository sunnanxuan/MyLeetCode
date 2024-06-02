class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res=0
        dic=collections.Counter(answers)
        for k in dic:
            if dic[k]<=(k+1):res+=(k+1)
            else:res+=(dic[k]//(k+1)+int(bool(dic[k]%(k+1))))*(k+1)
        return res