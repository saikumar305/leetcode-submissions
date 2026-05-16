class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:

        idx = self.hash(key)

        for pair in self.map[idx]:

            if pair[0] == key:
                pair[1] = value
                return

        self.map[idx].append([key, value])

    def get(self, key: int) -> int:

        idx = self.hash(key)

        for k, v in self.map[idx]:

            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:

        idx = self.hash(key)

        bucket = self.map[idx]

        for i in range(len(bucket)):

            if bucket[i][0] == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)