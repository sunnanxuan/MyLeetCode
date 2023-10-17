class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        res_set=set()
        for i in range(len(nums)+1):
            for c in itertools.combinations(nums,i):
                each=sorted(list(c))

                if tuple(each) not in res_set:
                    res.append(each)
                    res_set.add(tuple(each))
        return res