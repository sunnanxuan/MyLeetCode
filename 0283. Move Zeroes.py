class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=len(nums)
        i=0
        while i<l:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                l-=1
            else:
                i+=1


        """
        Do not return anything, modify nums in-place instead.
        """