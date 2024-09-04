class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(dict)
        self.keys = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key][timestamp] = value
        bisect.insort(self.keys[key], timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        elif timestamp not in self.dic[key]:
            t = self.keys[key]
            p = bisect.bisect(t, timestamp)
            if p == 0:
                return ""
            else:
                return self.dic[key][t[p - 1]]
        else:
            return self.dic[key][timestamp]
