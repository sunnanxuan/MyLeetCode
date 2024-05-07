class MyHashMap:

    def __init__(self):
        self.hashset = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self.hashset[key] = value

    def get(self, key: int) -> int:
        return self.hashset[key]

    def remove(self, key: int) -> None:
        self.hashset[key] = -1