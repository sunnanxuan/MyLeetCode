class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        res=[]
        for n in deck:
            if not res:res.append(n)
            else:
                res.append(res.pop(0))
                res.append(n)
        return res[::-1]