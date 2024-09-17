class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        dic={}
        count=collections.defaultdict(int)
        res=0
        while r<len(nums):
            dic[nums[r]]=r
            count[nums[r]]+=1
            while len(count)>k:
                count[nums[l]]-=1
                if count[nums[l]]==0:
                    count.pop(nums[l])
                    dic.pop(nums[l])
                l+=1
            if len(dic)==k:
                mn=min(dic.values())
                res+=(mn-l+1)
            r+=1
        return res

