class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo=collections.defaultdict(int)
        def sumtarget(sm,i):
            if (sm,i) in memo:
                return memo[(sm,i)]
            elif i==0:
                if sm==nums[0]:
                    memo[(sm,i)]+=1
                if sm==-1*nums[0]:
                    memo[(sm,i)]+=1
                return memo[(sm,i)]
            elif i>0:
                memo[(sm,i)]+=sumtarget(sm+nums[i],i-1)
                memo[(sm,i)]+=sumtarget(sm-nums[i],i-1)
                return memo[(sm,i)]

        return sumtarget(target,len(nums)-1)
