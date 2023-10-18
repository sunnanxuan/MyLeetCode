class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        memo = {}

        def bfs(n, s):
            if (s, n) in memo:
                return memo[(s, n)]
            else:
                if len(s) > n * 3 or (not s and n >= 1):
                    memo[(s, n)] = False
                else:

                    if n == 1:
                        if int(s) <= 255:
                            if s[0] == '0' and len(s) > 1:
                                memo[(s, n)] = False
                            else:
                                memo[(s, n)] = [s]
                        else:
                            memo[(s, n)] = False
                    else:
                        lst = []
                        for i in range(1, 4):
                            if len(s) >= i and int(s[:i]) <= 255:
                                if i > 1 and s[0] == '0':
                                    continue

                                c = s[:i]
                                m = bfs(n - 1, s[i:])
                                if not m:
                                    continue
                                else:
                                    for p in m:
                                        lst.append(c + '.' + p)
                        if not lst:
                            memo[(s, n)] = False
                        else:
                            memo[(s, n)] = lst
                return memo[(s, n)]

        bfs(4, s)
        res = memo[(s, 4)]
        return res and res or []