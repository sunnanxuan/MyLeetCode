class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        m = n // 2 + n % 2
        dic = collections.Counter(s)
        arr = sorted(list(dic.items()), key=lambda x: -1 * x[1])
        if arr[0][1] > m:
            return ""
        else:
            string = []
            for k, v in arr:
                string.append(k * v)
            string = ''.join(string)
            lst = [['#', '#'] for _ in range(m)]
            for i in range(m):
                lst[i][0] = string[i]
                if i + m < n:
                    lst[i][1] = string[i + m]

            res = ''.join([a + b for a, b in lst])
            res = res.rstrip('#')
            return res
