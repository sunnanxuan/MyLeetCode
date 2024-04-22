class MagicDictionary:

    def __init__(self):
        self.dictionary = collections.defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            n = len(word)
            for i in range(n):
                s = word[:i] + '*' + word[i + 1:]
                self.dictionary[s].add(word)

    def search(self, searchWord: str) -> bool:
        l = len(searchWord)
        for i in range(l):
            w = searchWord[:i] + '*' + searchWord[i + 1:]
            if w in self.dictionary and (
                    len(self.dictionary[w]) > 1 or searchWord not in self.dictionary[w]): return True
        return False
