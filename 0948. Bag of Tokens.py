class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res=0
        score=0
        while tokens:
            while tokens and tokens[0]<=power:
                cur=tokens.pop(0)
                score+=1
                power-=cur
            res=max(res,score)
            if not score:return res
            if score and tokens:
                cur=tokens.pop()
                score-=1
                power+=cur
        return res

