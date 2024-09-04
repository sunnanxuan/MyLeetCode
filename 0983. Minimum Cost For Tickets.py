class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        for d in days:
            cur = float('inf')
            for i, c in enumerate([1, 7, 30]):
                p = bisect.bisect_right(days, d - c)
                if p <= 0:
                    t = costs[i]
                else:
                    t = dp[days[p - 1]] + costs[i]
                cur = min(cur, t)
            dp[d] = cur
        return dp[days[-1]]
