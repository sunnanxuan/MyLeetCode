class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = collections.defaultdict(int)
        self.times = collections.defaultdict(list)
        self.dic = {}

    def get(self, key):
        if key not in self.dic:
            return -1
        else:
            self.count[key] += 1
            if self.count[key] > 1:
                self.times[self.count[key] - 1].remove(key)
                if not self.times[self.count[key] - 1]:
                    self.times.pop(self.count[key] - 1)
            self.times[self.count[key]].append(key)
            return self.dic[key]

    def put(self, key, value):
        if key in self.dic:
            self.dic[key] = value
            self.count[key] += 1
            if self.count[key] > 1:
                self.times[self.count[key] - 1].remove(key)
                if not self.times[self.count[key] - 1]:
                    self.times.pop(self.count[key] - 1)
            self.times[self.count[key]].append(key)
        else:
            if len(self.dic) >= self.capacity:
                m = min(self.times.keys())
                k = self.times[m].pop(0)
                if not self.times[m]:
                    self.times.pop(m)
                self.count.pop(k)
                self.dic.pop(k)
            self.dic[key] = value
            self.count[key] += 1
            self.times[self.count[key]].append(key)



