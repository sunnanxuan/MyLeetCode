class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        arr=[]
        for i in range(min(indexDiff+1,len(nums))):
            arr.append(nums[i])
        arr.sort()
        diff=min([arr[i]-arr[i-1] for i in range(1,len(arr))])
        if diff<=valueDiff:
            return True
        for i in range(indexDiff+1,len(nums)):
            arr.remove(nums[i-indexDiff-1])
            p=bisect.bisect(arr,nums[i])
            if p==0:
                diff=arr[p]-nums[i]
            elif p==len(arr):
                diff=nums[i]-arr[p-1]
            else:
                diff=min(nums[i]-arr[p-1],arr[p]-nums[i])
            if diff<=valueDiff:
                return True
            bisect.insort(arr,nums[i])
        return False