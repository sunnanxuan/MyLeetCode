class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.dic = {}
        count = collections.defaultdict(int)
        for i in range(len(times)):
            count[persons[i]] += 1
            j = i
            m = max(count.values())
            while count[persons[j]] != m:
                j -= 1
            self.dic[times[i]] = persons[j]
        self.times = times

    def q(self, t: int) -> int:
        p = bisect.bisect_right(self.times, t) - 1
        c = self.times[p]
        return self.dic[c]
