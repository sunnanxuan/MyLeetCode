class MapSum:

    def __init__(self):
        self.strings = {}
        self.map = collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        if key not in self.strings:
            self.strings[key] = val
            for i in range(1, len(key) + 1):
                self.map[key[:i]] += val
        else:
            diff = val - self.strings[key]
            self.strings[key] = val
            for i in range(1, len(key) + 1):
                self.map[key[:i]] += diff

    def sum(self, prefix: str) -> int:
        return self.map[prefix]