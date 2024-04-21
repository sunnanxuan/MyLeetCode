class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        tails = collections.defaultdict(list)
        nums.sort()
        for n in nums:
            if n - 1 not in tails:
                bisect.insort(tails[n], n)
            else:
                s = tails[n - 1].pop()
                bisect.insort(tails[n], s)
                if not tails[n - 1]:
                    tails.pop(n - 1)
        return all([e - s > 1 for e in tails for s in tails[e]])
