class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def matchstring(t):
            for i in range(m - n + 1):
                if all([c == "?" for c in t[i:i + n]]):
                    continue
                elif all([a == b or b == '?' for a, b in zip(stamp, t[i:])]):
                    return i
            return -1

        res = []
        m = len(target)
        n = len(stamp)
        while any([c != '?' for c in target]):
            i = matchstring(target)
            if i == -1: return []
            res.append(i)
            target = target[:i] + '?' * n + target[i + n:]
        return res[::-1]