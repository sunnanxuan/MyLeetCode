class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = [limit] * len(people)
        people.sort(reverse=True)
        res = 0
        for w in people:
            p = bisect.bisect_left(boats, w)
            c = boats.pop(p)
            if c < limit:
                res += 1
            else:
                bisect.insort(boats, c - w)
        res += sum([n != limit for n in boats])
        return res
