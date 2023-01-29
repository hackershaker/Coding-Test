# 우선순위 큐를 이용하여 구현
# id값이 크면 더 최근 사용했다는 뜻
# count는 참조 횟수
# id, count값으로 최소 heap에서 least frequency 판별



from collections import defaultdict
from heapq import heappop, heappush
import itertools


class LFUCache:

    def __init__(self, capacity: int):
        self.iterator = itertools.count(0,1)
        self.capacity = capacity
        self.counter = defaultdict(int) # key : count
        self.currentKeyinCache = defaultdict(int) # key : id
        self.valueStorage = defaultdict(int)
        self.cache = [] # (count, id, key)

    def get(self, key: int) -> int:
        # print(f"GET {key}")
        if key not in self.currentKeyinCache:
            return -1
        else:
            self.counter[key] += 1
            newid = self.iterator.__next__()
            heappush(self.cache, (self.counter[key], newid, key))
            self.currentKeyinCache[key] = newid
            # print(self.currentKeyinCache)
            return self.valueStorage[key]

    def put(self, key: int, value: int) -> None:
        # print(f"PUT {key}")
        if key in self.currentKeyinCache:
            self.valueStorage[key] = value
            self.counter[key] += 1
            newid = self.iterator.__next__()
            heappush(self.cache, (self.counter[key], newid, key))
            self.currentKeyinCache[key] = newid
            return
        newid = self.iterator.__next__()
        if len(self.currentKeyinCache) == self.capacity:
            try:
                while True:
                    referenceNumber, id, leastUsedKey = heappop(self.cache)
                    if self.currentKeyinCache[leastUsedKey] == id:
                        # print("least used key: ", leastUsedKey)
                        del self.currentKeyinCache[leastUsedKey]
                        heappush(self.cache, (1, newid, key))
                        break
            except:
                return
        else:
            heappush(self.cache, (1, newid, key))
        self.valueStorage[key] = value
        self.currentKeyinCache[key] = newid
        self.counter[key] = 1
        # print(self.cache, self.currentKeyinCache)
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)