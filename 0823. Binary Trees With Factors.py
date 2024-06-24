class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        nums=set(arr)
        mod=10**9+7
        dic=collections.defaultdict(set)
        arr.sort()
        used=set
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if arr[i]*arr[j] in nums:
                    dic[arr[i]*arr[j]].add((i,j))
        dp=[1]*len(arr)
        for i in range(len(arr)):
            if arr[i] in dic:
                for x,y in dic[arr[i]]:
                    if x==y:dp[i]+=dp[x]*dp[y]
                    else:
                        dp[i]+=(dp[x]*dp[y])*2
                    dp[i]%=mod
        return sum(dp)%mod