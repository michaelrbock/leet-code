from collections import defaultdict, namedtuple


TimeValue = namedtuple('Value', ['timestamp', 'value'])


class TimeMap:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.time_map = defaultdict(list)  # key : [TimeValue]

  def _smallest_gte(self, lst, target):
    """Returns index of smallest timestamp in lst >= target in (sorted) lst.
    Or -1 if no such number exists. Using binary search O(logn) method.
    """
    start = 0
    end = len(lst) - 1
    while start <= end:
      mid = (start + end) // 2
      if target >= lst[mid].timestamp:
        start = mid + 1
      else:  # target < lst[mid].timestamp:
        end = mid - 1
    return start - 1

  def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
    # The timestamps for all TimeMap.set operations are strictly increasing.
    self.time_map[key].append(TimeValue(timestamp, value))

  def get(self, key: 'str', timestamp: 'int') -> 'str':
    index = self._smallest_gte(self.time_map[key], timestamp)
    if index == -1:
      return ""  # Not found.
    return self.time_map[key][index].value

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

kv = TimeMap()
kv.set("foo", "bar", 1) # store the key "foo" and value "bar" along with timestamp = 1
assert kv.get("foo", 1) == "bar"
kv.get("foo", 3) == "bar" # since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4)
assert kv.get("foo", 4) == "bar2"
assert kv.get("foo", 5) == "bar2"

["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
kv = TimeMap()
kv.set("love", "high", 10)
kv.set("love", "low", 20)
assert kv.get("love", 5) == ""
assert kv.get("love", 10) == "high"
assert kv.get("love", 15) == "high"
assert kv.get("love", 20) == "low"
assert kv.get("love", 25) == "low"
