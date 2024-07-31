class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        heap=[]
        heapq.heappush(heap,(0,0))
        visited={0}
        while heap:
            s,p=heapq.heappop(heap)
            for i in range(1,7):
                cur=p-i
                r=(-1*cur)//n
                if r%2==0:c=(-1*cur)%n
                else:c=n-1-(-1*cur)%n
                r=n-1-r
                if board[r][c]!=-1:
                    cur=-1*board[r][c]+1
                if -1*cur+1>=n**2:return s+1
                if cur not in visited:
                    heapq.heappush(heap,(s+1,cur))
                    visited.add(cur)
        return -1