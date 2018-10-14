"""
Backtracking.

Notes on IP Addresses:
* Each section separated by '.' can not start with '0', unless it's '0' alone.
* Each section separared by '.' can not be > 255.
"""


def valid(ip):
  sections = ip.split('.')
  if len(sections) != 4:
    return False
  for section in sections:
    if len(section) == 0 or len(section) > 3:
      return False
    if len(section) != 1 and section[0] == '0':
      return False
    if int(section) > 255:
      return False
  return True


def restore_rec(lst, start, to_place):
  if to_place == 0:
    ip = ''.join(lst)
    if valid(ip):
      return [ip]
  results = []
  for i in range(start, start + 3):
    if i >= len(lst):
      continue
    results.extend(restore_rec(lst[:i] + ['.'] + lst[i:], i + 2, to_place - 1))
  return results


class Solution:
  def restoreIpAddresses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    if len(s) < 4 or len(s) > 12:
      return []
    lst = list(s)
    results = []
    for i in range(1, 4):
      result = restore_rec(lst[:i] + ['.'] + lst[i:], i + 2, 2)
      if result:
        results.extend(result)
    return results
