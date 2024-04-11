class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1={}
        for i,c in enumerate(list1):
            dic1[c]=i
        res=[float('inf'),[]]
        for j,c in enumerate(list2):
            if c in dic1:
                if dic1[c]+j<res[0]:
                    res=[dic1[c]+j,[c]]
                elif dic1[c]+j==res[0]:
                    res[1].append(c)
        return res[1]