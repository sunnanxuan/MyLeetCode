class Solution:
    def numTrees(self, n: int) -> int:
        memo={}
        def count(l,r):
            if (l,r) in memo:
                return memo[(l,r)]
            elif l>=r:
                return 1
            else:
                c=0
                for i in range(l,r+1):
                    left=count(l,i-1)
                    right=count(i+1,r)
                    c+=(left*right)

                memo[(l,r)]=c
                return c
        return count(1,n)