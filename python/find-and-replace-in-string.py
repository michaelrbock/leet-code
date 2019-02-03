class Solution:
  def findReplaceString(self, S, indexes, sources, targets):
    """
    :type S: str
    :type indexes: List[int]
    :type sources: List[str]
    :type targets: List[str]
    :rtype: str
    """
    index_to_source = {}
    index_to_taret = {}
    for i in range(len(indexes)):
      index_to_source[indexes[i]] = sources[i]
      index_to_taret[indexes[i]] = targets[i]
    indexes.sort()

    new_s = []
    start, end = 0, 0
    for i in range(len(indexes)):
      index = indexes[i]
      source = index_to_source[index]
      target = index_to_taret[index]
      new_start, new_end = index, index + len(source)
      if S[new_start:new_end] != source:
        continue

      if new_start > end:
        new_s.append(S[end:new_start])
      start, end = new_start, new_end
      new_s.append(target)

    if end != len(S):
      new_s.append(S[end:])

    return ''.join(new_s)
