class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key in self.store:
            curr = self.store[key]
            l, r = 0, len(curr) - 1
            
            while l <= r:
                m = (l + r) // 2
                if curr[m][1] <= timestamp:
                    result = curr[m][0]
                    l = m + 1
                else:
                    r = m - 1
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)