class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l = []
        r = []
        for log in logs:
            arr = log.split()
            s = ''.join(arr[1:])
            if s.isalpha():
                l.append([arr[0], ' '.join(arr[1:])])
            else:
                r.append(log)
        l.sort(key=lambda x: (x[1], x[0]))
        res = []
        for c in l:
            res.append(' '.join(c))
        return res + r
