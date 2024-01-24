class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        m=len(nums)//2
        ins=copy.copy(nums[:m])
        nums[:]=nums[m:]
        i=1
        for n in ins:
            nums.insert(i,n)
            i+=2