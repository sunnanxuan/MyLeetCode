class LRUCache:

    def __init__(self, capacity: int):
        self.data={}
        self.capacity= capacity
        self.queue=[]

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        else:
            self.queue.remove(key)
            self.queue.append(key)
            return self.data[key]

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)
        if len(self.queue) > self.capacity:
            n=self.queue.pop(0)
            self.data.pop(n)