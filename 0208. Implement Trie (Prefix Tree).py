class Trie:

    def __init__(self):
        self.trie = []
        self.dic = collections.defaultdict(set)

    def insert(self, word: str) -> None:
        if word in self.trie:
            return
        else:
            self.trie.append(word)
            for i in range(1, len(word) + 1):
                self.dic[word[0]].add(word[:i])

    def search(self, word: str) -> bool:
        return word in self.trie

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.dic:
            return False
        else:
            return prefix in self.dic[prefix[0]]