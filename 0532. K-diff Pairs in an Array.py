class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k==0:
            dic=collections.Counter(nums)
            return sum([dic[k]>=2 for k in dic])
        else:
            res=0
            nums=sorted(list(set(nums)))
            for n in nums:
                if n+k in nums:
                    res+=1
            return res