class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy=[[0]*k for _ in range(len(prices))]
        sale=[[0]*k for _ in range(len(prices))]
        for i,p in enumerate(prices):
            if i==0:
                buy[0]=[-1*p]*k
            else:
                for j in range(k):
                    if j==0:
                        buy[i][j]=max(buy[i-1][j],0-p)
                    else:
                        buy[i][j]=max(buy[i-1][j],sale[i-1][j-1]-p)
                    sale[i][j]=max(sale[i-1][j],buy[i-1][j]+p)
        return sale[-1][-1]