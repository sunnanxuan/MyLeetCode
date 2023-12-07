class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        nums.sort(key=lambda x:x[0],reverse=True)
        def numsort(lst):
            change=True
            while change:
                change=False
                for i in range(len(lst)-1):
                    if lst[i]+lst[i+1]<lst[i+1]+lst[i]:
                        change=True
                        lst[i],lst[i+1]=lst[i+1],lst[i]
            return lst
        i=0
        while i<len(nums):
            j=i
            while j+1<len(nums) and nums[i][0]==nums[j+1][0]:
                j+=1
            nums[i:j+1]=numsort(nums[i:j+1])
            i=j+1
        return str(int(''.join(nums)))


