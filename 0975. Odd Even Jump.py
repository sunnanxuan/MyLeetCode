class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        inds = collections.defaultdict(list)
        for i in range(n):
            inds[arr[i]].append(i)
        lst = sorted(arr)
        jumps = []
        for c in arr:
            lst.remove(c)
            inds[c].pop(0)
            p = bisect.bisect_left(lst, c)
            if p < len(lst) and lst[p] == c:
                j = inds[c][0]
                jumps.append([j, j])
            else:
                if p < len(lst):
                    o = inds[lst[p]][0]
                else:
                    o = -1
                if p > 0:
                    e = inds[lst[p - 1]][0]
                else:
                    e = -1
                jumps.append([o, e])
        print(jumps)
        res = 1
        dp = [['unkonw', 'unkonw'] for _ in range(n)]
        dp[-1] = [True, True]
        for i in range(n - 2, -1, -1):
            m = 0
            cur = i
            # print("***********",i)
            while True:
                # print(cur,m,jumps[cur][m],dp)
                if jumps[cur][m] == -1:
                    break
                elif dp[jumps[cur][m]][(m + 1) % 2] == True:
                    # print('&&&&')
                    res += 1
                    dp[i][0] = True
                    break
                elif dp[jumps[cur][m]][(m + 1) % 2] == False:
                    dp[i][0] = False
                    break
                else:
                    cur = jumps[cur][m]
                    m += 1
                    m %= 2

        return res

