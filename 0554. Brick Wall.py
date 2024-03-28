class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        count = collections.defaultdict(int)
        for w in wall:
            l = 0
            for c in w:
                l += c
                count[l] += 1
            count[l] -= 1
        return n - max(count.values())
