class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        stack=[]
        for i in range(len(candidates)):
            if candidates[i]<target:
                stack.append([i,candidates[i],[candidates[i]]])
            elif candidates[i]==target:
                res.append([candidates[i]])
            elif candidates[i]>target:
                break
        while stack:
            i,sm,arr=stack.pop()
            for j in range(i,len(candidates)):
                if candidates[j]+sm==target:
                    res.append(arr+[candidates[j]])
                elif candidates[j]+sm<target:
                    stack.append([j,candidates[j]+sm,arr+[candidates[j]]])
                else:
                    break
        return res