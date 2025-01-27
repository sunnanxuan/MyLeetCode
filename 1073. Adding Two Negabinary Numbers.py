class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:

        res = []
        pre = 0
        while arr1 or arr2:
            if arr1:
                n1 = arr1.pop()
            else:
                n1 = 0
            if arr2:
                n2 = arr2.pop()
            else:
                n2 = 0
            cur = n1 + n2 + pre
            if cur == -1:
                res.append(1)
                pre = 1
            else:
                res.append(cur % 2)
                pre = -1 * (cur // 2)
        if pre == -1:
            res.append(1)
            res.append(1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return res[::-1]