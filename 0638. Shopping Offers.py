class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        res=[sum([price[i]*needs[i] for i in range(len(needs))])]
        def offer(needs,sm):
            if all(n==0 for n in needs):
                res[0]=min(res[0],sm)
            else:
                mp=sum([price[i]*needs[i] for i in range(len(needs))])
                res[0]=min(res[0],sm+mp)
                for s in special:
                    if sm+s[-1]<res[0]:
                        new=[needs[i]-s[i] for i in range(len(needs))]
                        if all(n>=0 for n in new):
                            offer(new,sm+s[-1])

        offer(needs,0)
        return res[0]