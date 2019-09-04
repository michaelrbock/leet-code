from collections import Counter
import heapq


class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    num_counts = Counter(nums)
    return heapq.nlargest(k, num_counts, key = lambda x: num_counts[x])
