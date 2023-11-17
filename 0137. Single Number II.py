class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic=collections.defaultdict(int)
        for n in nums:
            if dic[n]<2:
                dic[n]+=1
            else:
                dic.pop(n)
        return list(dic.keys())[0]