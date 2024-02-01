class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.Counter(nums)
        res=[]
        for n,c in dic.most_common(k):
            res.append(n)
        return res