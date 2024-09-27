class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for q in queries:
            i = 0
            j = 0
            for i in range(len(pattern)):
                while j < len(q) and q[j].islower() and pattern[i] != q[j]:
                    j += 1
                if j < len(q) and pattern[i] == q[j]:
                    j += 1
                else:
                    res.append(False)
                    break
            else:
                for k in range(j, len(q)):
                    if q[k].isupper():
                        res.append(False)
                        break
                else:
                    res.append(True)
        return res

