class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        memo=collections.defaultdict(set)
        def operation(m1,m2,op):
            if op=='+':return m1+m2
            elif op=='-':return m1-m2
            elif op=='*':return m1*m2
            elif op=='/':return m1/m2
        def compute(arr):
            if tuple(arr) in memo:
                return memo[tuple(arr)]
            if len(arr)==1:
                memo[tuple(arr)].add(arr[0])
                return memo[tuple(arr)]
            else:
                for i in range(1,len(arr)):
                    L=compute(arr[:i])
                    R=compute(arr[i:])
                    for l in L:
                        for r in R:
                            if r==0:
                                for op in '+-*':
                                    memo[tuple(arr)].add(operation(l,r,op))
                            else:
                                for op in '+-*/':
                                    memo[tuple(arr)].add(operation(l,r,op))
                return memo[tuple(arr)]

        for each in itertools.permutations(cards,4):
            lst=compute(list(each))
            for res in lst:
                if 23.999 <= res <= 24.0001:return True
        return False