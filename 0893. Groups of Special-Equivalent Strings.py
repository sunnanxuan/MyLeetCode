class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        arr=[]
        for w in words:
            odd=collections.defaultdict(int)
            even=collections.defaultdict(int)
            for i in range(0,len(w),2):
                odd[w[i]]+=1
                if i+1<len(w):
                    even[w[i+1]]+=1
            o=tuple(sorted(list(odd.items())))
            e=tuple(sorted(list(even.items())))
            arr.append((o,e))
        c=collections.Counter(arr)
        return len(c)