class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sm=sum(arr)
        if sm%3:return False
        sm1=arr[0]
        i=1
        while i<len(arr) and sm1!=sm//3:
            sm1+=arr[i]
            i+=1
        if i==len(arr):return False
        sm2=arr[i]
        i+=1
        while i<len(arr) and sm2!=sm//3:
            sm2+=arr[i]
            i+=1
        if i==len(arr):return False
        return True
