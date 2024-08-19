class Solution:
    def knightDialer(self, n: int) -> int:
        if n==1:return 10
        dial={1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[2,6],8:[1,3],9:[4,2],0:[4,6]}
        dic={1:1,2:1,3:1,4:1,6:1,7:1,8:1,9:1,0:1}
        for i in range(n-1):
            new=collections.defaultdict(int)
            for k in dic:
                for m in dial[k]:
                    new[m]+=dic[k]
            dic=new
        mod=10**9+7
        return sum(dic.values())%mod