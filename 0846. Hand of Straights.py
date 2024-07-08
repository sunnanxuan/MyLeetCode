class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:return False
        dic=collections.Counter(hand)
        while dic:
            mn=min(dic.keys())
            cur=mn
            for i in range(groupSize):
                if cur in dic:
                    dic[cur]-=1
                    if dic[cur]==0:dic.pop(cur)
                else:return False
                cur+=1
        return True
