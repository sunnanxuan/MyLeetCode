class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        arr = []
        pre = cur = 1
        n = 0
        while cur < label:
            arr.append((pre, cur))
            n += 1
            pre = cur + 1
            cur += 2 ** n

        res = [label]
        while label > 1:
            l, r = arr.pop()
            label //= 2
            label = l + (r - label)
            res.append(label)
        return res[::-1]








