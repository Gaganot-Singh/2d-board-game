
class HashTable:
    def __init__(self, cap=32):
        self.cap = cap
        self.myTable = [None] * cap

    def insert(self, key, value):
        index = hash(key) % self.cap

        if self.myTable[index] is None:
            self.myTable[index] = []

        for pair in self.myTable[index]:
            if pair and pair[0] == key:
                return False

        self.myTable[index].append([key, value])

        numOfEles = sum(len(bucket) for bucket in self.myTable if bucket)
        loadFactor = numOfEles / self.cap

        if loadFactor > 0.7:
            self._resize()

        return True

    def _resize(self):
        oldTable = self.myTable
        self.cap *= 2
        self.myTable = [None] * self.cap
        for bucket in oldTable:
            if bucket:
                for key, value in bucket:
                    self.insert(key, value)

    def modify(self, key, value):
        for bucket in self.myTable:
            if bucket:
                for pair in bucket:
                    if pair[0] == key:
                        pair[1] = value
                        return True
        return False

    def remove(self, key):
        for bucket in self.myTable:
            if bucket:
                for pair in bucket:
                    if pair[0] == key:
                        bucket.remove(pair)
                        return True
        return False

    def search(self, key):
        for bucket in self.myTable:
            if bucket:
                for pair in bucket:
                    if pair[0] == key:
                        return pair[1]
        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return sum(len(bucket) for bucket in self.myTable if bucket)
