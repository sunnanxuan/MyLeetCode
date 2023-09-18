class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i,n in enumerate(nums):
            if target-n not in dic:
                dic[n]=i
            else:
                return [dic[target-n],i]