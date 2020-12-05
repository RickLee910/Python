class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.len = capacity
        self.temp = []

    def get(self, key: int) -> int:
        if key in self.dic.keys():
            if key in self.temp:
                self.temp = self.temp[:self.temp.index(key)]  +self.temp[self.temp.index(key)+1:]+ [ key]
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if len(self.dic) == self.len and key not in self.dic.keys():

            self.dic.pop(self.temp.pop(0))


        if key not in self.dic.keys():
            self.temp.append(key)
        else:
            self.temp = self.temp[:self.temp.index(key)] + self.temp[self.temp.index(key) + 1:] + [key]

        self.dic[key] = value
s = LRUCache(2)
s.put(2,6)

s.get(1)
s.put(1,5)
s.put(1,2)
s.get(1)

s.get(2)
