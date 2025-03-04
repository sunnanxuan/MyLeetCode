class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        dp = [[0, ''] for _ in range(l1 + 1)]
        for j in range(l2):
            new = [[0, ''] for _ in range(l1 + 1)]
            for i in range(l1):
                if str1[i] == str2[j]:
                    m = max(dp[i][0] + 1, dp[i + 1][0], new[i][0])
                    if m == dp[i][0] + 1:
                        new[i + 1][0] = dp[i][0] + 1
                        new[i + 1][1] = dp[i][1] + str2[j]
                    elif m == dp[i + 1][0]:
                        new[i + 1][0] = dp[i + 1][0]
                        new[i + 1][1] = dp[i + 1][1]
                    else:
                        new[i + 1][0] = new[i][0]
                        new[i + 1][1] = new[i][1]

                else:
                    m = max(dp[i + 1][0], new[i][0])
                    if m == dp[i + 1][0]:
                        new[i + 1][0] = dp[i + 1][0]
                        new[i + 1][1] = dp[i + 1][1]
                    else:
                        new[i + 1][0] = new[i][0]
                        new[i + 1][1] = new[i][1]
            dp = new

            # print(dp)

        s = dp[-1][-1]
        inserts = [''] * (len(s) + 1)

        def insertletters(str):
            i = j = 0
            while j < len(str):
                if i == len(s):
                    inserts[i] += str[j]
                    j += 1
                else:
                    if str[j] == s[i]:
                        i += 1
                        j += 1
                    else:
                        inserts[i] += str[j]
                        j += 1

        # print(s)
        insertletters(str1)
        insertletters(str2)
        res = []
        res.append(inserts.pop(0))
        for c in s:
            res.append(c)
            res.append(inserts.pop(0))
        return ''.join(res)






