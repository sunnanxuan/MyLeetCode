class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        memo = {}
        if l1 + l2 != l3:
            return False

        def match(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            b1 = b2 = False
            if i == l1 and j == l2 and k == l3:
                memo[(i, j, k)] = True
                return True
            if i < l1 and k < l3 and s1[i] == s3[k]:
                b1 = match(i + 1, j, k + 1)
            if j < l2 and k < l3 and s2[j] == s3[k]:
                b2 = match(i, j + 1, k + 1)
            res = b1 or b2
            memo[(i, j, k)] = res
            return res

        match(0, 0, 0)
        return memo[(0, 0, 0)]

