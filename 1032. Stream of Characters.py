class StreamChecker:

    def __init__(self, words: List[str]):
        self.steam = []
        self.suffix = collections.defaultdict(dict)
        for word in words:
            w = word[::-1]
            cur = self.suffix[w[0]]
            for c in w[1:]:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = '#'

    def query(self, letter: str) -> bool:
        self.steam.append(letter)
        # print(self.steam)
        if letter not in self.suffix:
            return False
        else:
            cur = self.suffix[letter]

            i = len(self.steam) - 2
            while i >= 0:
                # print(cur)
                if '#' in cur:
                    return True
                elif self.steam[i] not in cur:
                    return False
                else:
                    cur = cur[self.steam[i]]
                    i -= 1
            return '#' in cur

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)