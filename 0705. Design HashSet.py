class MyHashSet:

    def __init__(self):
        self.hashset = [-1] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.hashset[key] = 1

    def remove(self, key: int) -> None:
        if self.hashset[key] == 1:
            self.hashset[key] = -1

    def contains(self, key: int) -> bool:
        return self.hashset[key] == 1
