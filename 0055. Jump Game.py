class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur=last=0
        while cur<=last:
            last=max(last,cur+nums[cur])
            if last>=len(nums)-1:
                return True
            cur+=1
        return False