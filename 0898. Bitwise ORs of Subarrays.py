class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        q={arr[0]}
        p={arr[0]}
        for i in range(1,len(arr)):
            new=set()
            for n in p:
                new.add(n|arr[i])
            new.add(arr[i])
            p=new
            q|=new
        return len(q)