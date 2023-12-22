class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
      if not nums:
        return []
      i=0
      res=[]
      while i<len(nums):
        s=str(nums[i])
        j=i+1
        while j<len(nums) and nums[j]-nums[j-1]==1:
          j+=1
        if j==i+1:
          res.append(s)
        else:
          res.append(s+'->'+str(nums[j-1]))
        i=j
      return res
