'''

design a hashmap where the key is some key and the value pair is a list of different timestamps

- time stamp initlizes the object of the ds
-  the set function does:
    - stores the key with some value at a given timestamp {key: [value:timeStamp]?}
- get takes in a key we return, where we return the key is the other parameter timestamp <= key's timestamp. If the key has many such values return the greatest value associated with its timestamp. If none exist return ''

'''

from collections import defaultdict

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key, value, timestamp):
        self.hashMap[key].append((timestamp, value))

    def get(self, key, timestamp):
        arr = self.hashMap.get(key, [])
        l, r = 0, len(arr)-1
        res = ""

        while l <= r:
            m = (l+r) //2
            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m+1
            else:
                r = m-1
        
        return res
        
