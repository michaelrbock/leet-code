# Definition for an interval.
# class Interval:
#   def __init__(self, s=0, e=0):
#     self.start = s
#     self.end = e

class Solution:
  def merge(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    result = []
    if not intervals or not intervals[0]:
      return result
    intervals.sort(key=lambda i: i.start)
    interval_start = intervals[0].start
    interval_end = intervals[0].end
    for index, interval in enumerate(intervals):
      if index == 0:
        continue
      if interval.start <= interval_end:
        interval_end = max(interval_end, interval.end)
      else:
        result.append(Interval(interval_start, interval_end))
        interval_start = interval.start
        interval_end = interval.end
    if not result or result[-1].start != interval_start:
      result.append(Interval(interval_start, interval_end))
    return result
