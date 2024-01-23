class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = copy.copy(primes)
        seen = set(nums)
        t = 1
        res = 1
        while t < n:
            c = heapq.heappop(nums)
            t += 1
            res = c
            for f in primes:
                if f <= c and f * c not in seen:
                    heapq.heappush(nums, f * c)
                    seen.add(f * c)
                elif f > c:
                    break
        return res

